# greetings/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("welcome/", views.welcome, name="welcome_alt"),
]
