from django.shortcuts import render
from . import views
from django.contrib.auth.decorators import login_required
from .models import Image, Profile, Comments
from .forms import SignupForm, ImageForm, ProfileForm, CommentForm



# Create your views here.
@login_required(login_url='/accounts/register/')
def index(request):
    return render(request,'index.html')
