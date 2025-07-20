from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def show_messages(request):
    messages = Message.objects.all().order_by('-sent_at')
    return render(request, 'greetings/messages.html', 
{'messages': messages})
