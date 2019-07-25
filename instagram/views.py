from django.shortcuts import render
from . import views


# Create your views here.
def welcome(request):
    return render(request,'index.html')
