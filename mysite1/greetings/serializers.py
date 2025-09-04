from rest_framework import serializers
from .models import Patient, Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'  

class PatientSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()  # Nested serialization for the related doctor

    class Meta:
        model = Patient
        fields = '__all__'
        
    