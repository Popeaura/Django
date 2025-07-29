from django import path 
from.import views

urlpatterns = [
    path('', views.welcome, name= 'welome'),
]
