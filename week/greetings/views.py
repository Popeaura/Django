from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def welcome(request):
    context = {'name':'Django Guru',
               'hobbies':['coding', 'music', 'gaming']
               }
    return render(request, 'greetings/welcome.html' , context)