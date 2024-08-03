from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Patient, Doctor

class PatientSignUpForm(UserCreationForm):
    profile_picture = forms.ImageField(required=False)
    address_line1 = forms.CharField(max_length=255)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    pincode = forms.CharField(max_length=10)
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'profile_picture', 'email', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        if commit:
            user.save()
            profile_picture = self.cleaned_data.get('profile_picture')
            Patient.objects.create(
                user=user, 
                profile_picture=self.cleaned_data['profile_picture'],
                address_line1=self.cleaned_data['address_line1'], 
                city=self.cleaned_data['city'], 
                state=self.cleaned_data['state'], 
                pincode=self.cleaned_data['pincode']
            )
        return user

class DoctorSignUpForm(UserCreationForm):
    profile_picture = forms.ImageField(required=False)
    address_line1 = forms.CharField(max_length=255)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    pincode = forms.CharField(max_length=10)
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'profile_picture', 'email', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True
        if commit:
            user.save()
            profile_picture = self.cleaned_data.get('profile_picture')
            Doctor.objects.create(
                user=user, 
                profile_picture=self.cleaned_data['profile_picture'],
                address_line1=self.cleaned_data['address_line1'], 
                city=self.cleaned_data['city'], 
                state=self.cleaned_data['state'], 
                pincode=self.cleaned_data['pincode']
            )
        return user
