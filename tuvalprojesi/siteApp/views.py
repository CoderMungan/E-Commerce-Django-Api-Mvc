from django.shortcuts import render, redirect
from .models import Tasarim

# djangonun user modelini dahil et
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):

    context = {}
    urunler = Tasarim.objects.all()
    context['urunler'] = urunler

    # Arama post geçiliyor
    if request.method == 'POST':
        arama = request.POST.get('search')
        # Post geldiyse ve boş değil ise
        if arama.len():
            searchUrun = Tasarim.objects.filter(sanatEseriBaslik = arama).first()
            context['searchUrunler'] = searchUrun
            print("Gelen veri:" ,searchUrun)
            
            
    return render(request, 'index.html', context)


