from django.contrib.auth.models import User
from django import forms
from .models import Patient
from django.forms import ModelForm

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password'}),
        )
    
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Username'}),
        )
    class Meta:
        model = User
        fields = ['username', 'password']

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'age', 'address', 'phone', 'gender',]

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False)

class NursePatientUpdateForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['systolic', 'diastolic', 'temperature', 'height',]

class NurseManagePatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['systolic', 'diastolic', 'temperature', 'height', 'nurse_name',]

class DoctorManagePatientForm(ModelForm):
    
    doctor_prescription = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'style': 'color: black;', 
                'placeholder': 'Doctor\'s prescription',
                },
        )
    )

    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'style': 'color: black;', 
                'placeholder': 'Doctor\'s comment',
                 'rows': 6, 'cols': 40, 
                },
        )
    )
    class Meta:
        model = Patient
        fields = ['doctor_prescription', 'comment', 'doctor_name',]