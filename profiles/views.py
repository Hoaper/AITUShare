from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def index(request):
    # Need to redirect user into his page or login page
    if request.session.get('login', False):
        return redirect('profile_personal', profile_login=request.session.get('login'))
    else:
        return redirect('index')


def profile(request, profile_login=None):

    user_profile = Profile.objects.filter(login__exact=profile_login)
    if user_profile:
        return render(request, 'profile.html', {"profile": user_profile[0]})
    return redirect('index')
