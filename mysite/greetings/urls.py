from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('',view.show_messages, name='show_messages' ),
]
