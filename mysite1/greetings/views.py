from django.shortcuts import render
from .models import Doctor, Patient

def patients_list(request):
    patients = Patient.objects.all()
    return render(request, "greetings/patients_list.html", {"patients": patients})

def doctors_list(request):
    doctors = Doctor.objects.all()
    return render(request, "greetings/doctors_list.html", {"doctors": doctors})
