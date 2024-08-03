from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signup/patient/', views.patient_signup, name='patient_signup'),
    path('signup/doctor/', views.doctor_signup, name='doctor_signup'),
    path('login/', views.login_view, name='login'),
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
]
