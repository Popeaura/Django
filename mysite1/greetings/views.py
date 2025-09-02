from django.shortcuts import render
from django.http import HttpResponse
from .models import Message  

def welcome(request):
    messages = Message.objects.all()
    context = {"messages": messages}
    return render(request, "greetings/message_list.html", context)
