from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('login_staff/', views.login_staff, name='login_staff'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('nurse_view/', views.nurse_view, name='nurse_view'),
    path('doctor_view/', views.doctor_view, name='doctor_view'),
    path('nurse_view/register_patients/', views.register_patients, name='register_patients'),
    path('nurse_view/search_patient/', views.search_patient, name='search_patient'),
    path('nurse_view/search_patient/nurse_update_patient/<int:pk>/', views.nurse_update_patient, name='nurse_update_patient'),
    path('doctor_view/doctor_search_patient/', views.doctor_search_patient, name='doctor_search_patient'),
    path('doctor_view/doctor_search_patient/doctor_update_patient/<int:pk>/', views.doctor_update_patient, name='doctor_update_patient'),
    path('doctor_view/doctor_register_patients/', views.doctor_register_patients, name='doctor_register_patients'),
    path('login_staff/error/', views.error, name='error'),
]
