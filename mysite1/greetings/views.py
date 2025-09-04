from django.shortcuts import render
from django.http import HttpResponse
from .models import Doctor, Patient
def patients_list(request):
    patients = Patient.objects.all()
    if patients.exists():
        return HttpResponse(", ".join([patient.name for patient in patients]))
    else:
        return HttpResponse("No patients found.")

def doctors_list(request):
    doctors = Doctor.objects.all()
    if doctors.exists():
        return HttpResponse(", ".join([doctor.name for doctor in doctors]))
    else:
        return HttpResponse("No doctors found.")
