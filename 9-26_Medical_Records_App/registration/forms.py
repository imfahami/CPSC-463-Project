from django import forms
from django.forms import ModelForm
from .models import Patient, Doctor


class PatientSignIn(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['username', 'password']


class DoctorSignIn(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['username', 'password']


class PatientSignUp(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'username', 'password', 'email']
