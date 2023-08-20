from django.shortcuts import render, redirect

# djangonun user modelini dahil et
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):

    # Arama post geçiliyor
    if request.method == 'POST':
        arama = request.POST.get('search')
        # Post geldiyse ve boş değil ise
        if arama.__len__:
            print('Post Çalışıyor')
    # Buradan sql yollacağız şuan da pass!


    return render(request, 'index.html')


