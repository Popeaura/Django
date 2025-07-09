from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def goodbye(request):
    return HttpResponse('It was nice meeting you tchuss !')
