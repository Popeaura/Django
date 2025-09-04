from django.shortcuts import render
from django.http import HttpResponse
from .models import Doctor, Patient

def patients_list(request):
    patients = Patient.objects.all()
    return HttpResponse(", ".join([patient.name for patient in patients]))  

def doctors_list(request):
    doctors = Doctor.objects.all()
    return HttpResponse(", ".join([doctor.name for doctor in doctors]))   