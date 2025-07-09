from django.shortcuts import render
from django.http import HttpResponse
from .models import Message

# Create your views here.
def hello_world(request):
    messages = Message.objects.all().order_by('-sent_at')
    context = {'name': 'Ahura pope', 'messages': messages}
    return render(request,'hello/greeting.html', context)


