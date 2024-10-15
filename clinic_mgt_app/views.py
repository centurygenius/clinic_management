from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from .forms import PatientForm, SearchForm, NurseManagePatientForm, DoctorManagePatientForm
from .models import Patient
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



# Create your views here.
def index(request):
    #Displays the index page
    return render(request, 'index.html')
    
def login_staff(request):
    #Displays the login page for staff based on staff category

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        staff_category = request.POST.get('staff')
        user = authenticate(request,username=username, password=password)
       
        if user is not None: #If user exists in the database, check if credentials are correct
            
            if staff_category == 'nurse':
                login(request, user)
                return redirect('nurse_view')
            elif staff_category == 'doctor':
                login(request, user)
                return redirect('doctor_view')
            else:
                messages.info(request, 'Invalid credentials!')
                return redirect('login_staff')
        else:
            messages.info(request, 'Invalid credentials!')
            return redirect('login_staff')
    else:
        return render(request, 'login_staff.html')

@login_required(login_url='login_staff')
def user_logout(request):
    #Logs out the user
    logout(request)
    return redirect('index')

@login_required(login_url='login_staff')
def reset_password(request):
    #Displays the reset password page and ensures only authenticated users can
    #reset their password

    if not request.user.is_authenticated:
        return redirect('login_staff')
    
    if request.method == 'POST':
        
        if request.POST.get('password') != request.POST.get('confirm_password'):
            messages.info(request, 'Passwords do not match')
            return redirect('reset_password')
        else:
            password = request.POST.get('password')
            request.user.set_password(password)
            request.user.save()
            messages.info(request, 'Password reset successfully')
            return redirect('login_staff')
    else:
        return render(request, 'reset_password.html')
@login_required(login_url='login_staff')
def nurse_view(request):
    #Displays the nurse station page and ensures only authenticated users can
    #access the page for health care service delivery

    if not request.user.is_authenticated:
        return redirect('login_staff')
    return render(request, 'nurse_view.html')

@login_required(login_url='login_staff')
def doctor_view(request):
    #Displays doctor's page and ensures only authenticated users can
    #access the page for health care service delivery   
    return render(request, 'doctor_view.html')
@login_required(login_url='login_staff')
def register_patients(request):
    #Displays the register patients page and ensures only authenticated users can
    #register patients

    if not request.user.is_authenticated:
        return redirect('login_staff')

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Patient registered successfully')
            return redirect('register_patients')
        else:
            form = PatientForm()
            messages.info(request, 'Patient registration failed')
            return render(request, 'register_patients.html', {'form': form})
    else:
        form = PatientForm()
        return render(request, 'register_patients.html', {'form': form})
@login_required(login_url='login_staff')    
def nurse_update_patient(request, pk):
    #Displays the update patient page and ensures only authenticated users can
    #update patient's information

    patient = Patient.objects.get(id=pk)
    form = NurseManagePatientForm(instance=patient)
    context = {
            'form': form
    }

    if request.method == 'POST':
        form = NurseManagePatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('nurse_view')
        print(request.POST)
    context = {
        'form': form
    }
    return render(request, 'nurse_update_patient.html', context)
@login_required(login_url='login_staff')
def search_patient(request):
    #Displays the search patient page for a nurse

    form = SearchForm()
    context = {
        'form': form
    }
    results = None

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # Example: Searching in 'first_name' and 'last_name' fields
            results = Patient.objects.filter(first_name__icontains=query) | Patient.objects.filter(last_name__icontains=query) | Patient.objects.filter(hospital_id__icontains=query)
        
    return render(request, 'search_patient.html', {'form': form, 'results': results})
@login_required(login_url='login_staff')
def doctor_search_patient(request):
    #Displays the search patient page for a doctor

    form = SearchForm()
    context = {
        'form': form
    }
    results = None

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # Example: Searching in 'first_name' and 'last_name' fields
            results = Patient.objects.filter(first_name__icontains=query) | Patient.objects.filter(last_name__icontains=query) | Patient.objects.filter(hospital_id__icontains=query)
        
    return render(request, 'doctor_search_patient.html', {'form': form, 'results': results})
@login_required(login_url='login_staff')
def doctor_update_patient(request, pk):
    #Displays the update patient page and ensures only authenticated users can
    #update patient's information

    patient = Patient.objects.get(id=pk)
    form = DoctorManagePatientForm(instance=patient)
    context = {
            'form': form
    }

    if request.method == 'POST':
        form = DoctorManagePatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('doctor_view')
        print(request.POST)
    context = {
        'form': form
    }
    return render(request, 'doctor_update_patient.html', context)
@login_required(login_url='login_staff')
def doctor_register_patients(request):
    #Displays the register patients page and ensures only authenticated users can
    #register patients

    if not request.user.is_authenticated:
        return redirect('login_staff')

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Patient registered successfully')
            return redirect('register_patients')
        else:
            form = PatientForm()
            messages.info(request, 'Patient registration failed')
            return render(request, 'register_patients.html', {'form': form})
    else:
        form = PatientForm()
        return render(request, 'register_patients.html', {'form': form})