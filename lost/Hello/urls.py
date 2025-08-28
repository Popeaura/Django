form django.urls import path
from . views

urlpatterns = [
    path('', views.hello_world, name='hello-world'),
]