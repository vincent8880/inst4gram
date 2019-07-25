from django.shortcuts import render
from . import views
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    return render(request,'index.html')
