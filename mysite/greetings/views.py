from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def welcome(request):
    context = {
        'name':'Kyler Gray',
        'hobbies':['coding','video games','Music', 'Travelling' ]
    }
    return render (request, 'greetings/welcome.html,context')