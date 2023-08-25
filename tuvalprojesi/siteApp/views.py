from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Tasarim, Hakkimizda, Iletisim, YorumYap

# djangonun user modelini dahil et
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout 


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

    context = {}

    urunler = Tasarim.objects.all()
    
    context['urunler'] = urunler

    return render(request, "urunler.html", context)


def iletisim(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Iletisim.objects.create(name = name, email = email, mesajKonusu = subject, mesajinIcerigi = message)

        return redirect('home')
    else:
        return render(request, "iletisim.html")


def urundetay(request, urunId):

    urunDetay = {}

    dbFilter = Tasarim.objects.filter(id = urunId).first()

    urunDetay['urunDetayi'] = dbFilter

    if request.method == "POST":
        yorumBaslik = request.POST.get('yorumBaslik')
        yorumIcerik = request.POST.get('yorumIcerik')
        YorumYap.objects.create(urun = dbFilter, yorumSahibi = request.user, yorumBaslik = yorumBaslik, yorumIcerik = yorumIcerik)
        return redirect('urundetay', urunId)

    urunveyorum = YorumYap.objects.filter(urun__id = urunId).all()
    urunDetay["yorumlar"] = urunveyorum


    return render(request, "urundetay.html" , urunDetay)


def login(request):

    if request.method == "POST":

        kullaniciAdi = request.POST.get('k-username')
        kullaniciSifre = request.POST.get('k-sifre')

        if kullaniciAdi and kullaniciSifre:
            user = authenticate(request, username = kullaniciAdi, password = kullaniciSifre)

            if user is not None:
                auth_login(request, user)
                return redirect("home")
            
            else:
                return redirect('login')
            
        else:
            return redirect('login')
            

    return render(request, "login.html")


def singup(request):

    if request.method == "POST":

        kullaniciAdi = request.POST.get("k-kullanici")
        kullaniciSifre = request.POST.get("k-sifre")
        kullaniciEmail = request.POST.get("k-email")

        if kullaniciSifre and kullaniciAdi and kullaniciEmail:
            kayitliMi = User.objects.filter(username = kullaniciAdi).first()

            if kayitliMi:
                return redirect('singup')
            else:
                User.objects.create_user(username = kullaniciAdi, password = kullaniciSifre, email = kullaniciEmail)
                return redirect('login')
        else:
            return redirect('singup')

    return render(request, "singup.html")



def cikis(request):

    logout(request)
    
    return redirect('home')