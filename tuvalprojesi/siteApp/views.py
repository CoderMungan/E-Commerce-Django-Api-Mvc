from django.shortcuts import render, redirect

# djangonun user modelini dahil et
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    
    return render(request, 'index.html')
