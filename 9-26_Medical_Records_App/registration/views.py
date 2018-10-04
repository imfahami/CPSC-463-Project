from django.shortcuts import render
from .forms import PatientSignIn, DoctorSignIn, PatientSignUp


# Create your views here.
def patient_login(request):
    form = PatientSignIn()
    return render(request, 'landing_page.html', {'form': form})


def doctor_login(request):
    form = DoctorSignIn()
    return render(request, 'doctor_landing.html', {'form': form})


def patient_signup(request):
    if request.method == 'POST':
        form = PatientSignUp(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = PatientSignUp()
    return render(request, 'landing_page.html', {'form': form})
