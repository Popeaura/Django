from django.urls import path
from . import views

urlpatterns = [
    path("api/patients/", views.patients_list, name="api-patients_list"),
    path("api/doctors/", views.doctors_list, name="api-doctors_list"),
]
