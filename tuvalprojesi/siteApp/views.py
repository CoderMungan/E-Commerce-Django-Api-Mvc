from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Tasarim, Hakkimizda

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
        if arama.__len__():
            searchUrun = Tasarim.objects.filter(Q(sanatEseriBaslik__icontains = arama)).all()
            context['searchUrunler'] = searchUrun

    return render(request, 'index.html', context)


def hakkimizda(request):

    icerik = {}

    db = Hakkimizda.objects.all()

    icerik['hakkimizdaVeri'] = db

    return render(request, "hakkimizda.html", icerik)


def urunler(request):

    return render(request, "urunler.html")
