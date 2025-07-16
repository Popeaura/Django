from django.shortcuts import render
from django.http import HttpResponse 
from .models import Message

# Create your views here.
def welcome(request):
    context = {
        'name':'Gray',
        'hobbies':['coding','video games','Music', 'Travelling' ]
    }
    return render (request, 'greetings/welcome.html',context)

def show_messages(request):
    messages = Message.objects.all().order_by('-sent_at')
    return render(request, 'greetings/messages.html', {'messaages' : messages})