from django.shortcuts import render
from django.conf.urls import url
from . import views


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')
