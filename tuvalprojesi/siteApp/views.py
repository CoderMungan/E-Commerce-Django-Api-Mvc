from django.shortcuts import render, redirect
from .models import Urun, Hakkimizda, Iletisim, YorumYap, ProfileModel, Katagori, Sepet

# djangonun user modelini dahil et
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout 


from .form import *

# Create your views here.
def index(request):

    context = {}
    urunler = Urun.objects.all()
    context['urunler'] = urunler
    
    kategoriler = Katagori.objects.all()
    context['kategoriler'] = kategoriler

    # Arama post geçiliyor

    return render(request, 'index.html', context)

def searchBar(request):

    context = {}

    if request.method == 'POST':
        arama = request.POST.get('search')
        # Post geldiyse ve boş değil ise
        print("index fn:", arama)
        if arama:
            searchUrun = Urun.objects.filter(urunBaslik__icontains = arama).all()   
            context['searchUrunler'] = searchUrun
        elif arama == "":
            return redirect('home')
    return render(request, 'index.html' ,context)


def hakkimizda(request):

    icerik = {}

    db = Hakkimizda.objects.all()

    icerik['hakkimizdaVeri'] = db

    return render(request, "hakkimizda.html", icerik)


def urunler(request):

    context = {}

    urunler = Urun.objects.all()
    
    context['urunler'] = urunler

    return render(request, "urunler.html", context)


def iletisim(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Iletisim.objects.create(name = name, email = email, mesajKonusu = subject, mesajinIcerigi = message)
        return redirect('iletisim')
    else:
        return render(request, "iletisim.html")

def sepet(request,urunId):

    urun = Urun.objects.get(id=urunId)
    if request.user.is_authenticated:
        Sepet.objects.create(urun = urun, user = request.user, sepeteAtilma = True, adet = +1)
        return redirect('urundetay', urunId)

    return redirect('urundetay',urunId)




def urundetay(request, urunId):

    urunDetay = {}
    urun_detay = Urun.objects.filter(id = urunId).first()
    urunDetay['urunDetayi'] = urun_detay

    yorum_detay = YorumYap.objects.filter(urun__id = urunId).all()
    urunDetay['yorumlar'] = yorum_detay
    # Hocaya Sorulacak!
    profile = ProfileModel.objects.filter(profileSahibi__id = request.user.id).first()

    if request.method == 'POST':
        yorumbaslik = request.POST.get('yorum-baslik')
        yorumaciklama = request.POST.get('yorum-aciklama')
        YorumYap.objects.create(yorumSahibiProfile = profile, urun = urun_detay, yorumSahibi = request.user, yorumBaslik = yorumbaslik, yorumIcerik = yorumaciklama)
        return redirect('urundetay',urunId)

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
                user = User.objects.create_user(username = kullaniciAdi, password = kullaniciSifre, email = kullaniciEmail)
                # bu usere profil ata
                ProfileModel.objects.create(profileSahibi = user)
                return redirect('login')
        else:
            return redirect('singup')

    return render(request, "singup.html")



def yorumSil(request, urunId, yorumId):

    if request.user:
        silinecek = YorumYap.objects.filter(id = yorumId, yorumSahibi = request.user).first()
        if silinecek is not None:
            silinecek.delete()
            return redirect('urundetay', urunId)
        elif request.user.is_superuser:
            silinecekAdmin = YorumYap.objects.filter(id = yorumId).first()
            silinecekAdmin.delete()
            return redirect('urundetay', urunId)

    return redirect('404')



def errorpage(request):

    return render(request, '404.html')



def cikis(request):

    logout(request)
    
    return redirect('home')



def profile(request, profileID):

    context = {}

    userFilter = User.objects.filter(id = profileID).first()

    if userFilter:
    
        context['kullanicilar'] = userFilter

        yorumlar = YorumYap.objects.filter(yorumSahibi__id = profileID).all()

        context['yorumlar'] = yorumlar

        profileFront = ProfileModel.objects.filter(profileSahibi__id = profileID).all()

        context['profiller'] = profileFront

    else:
        context["error"] = "Böyle bir user bulunamadi"


    # Update yapmaya çalışıyorum
    # profileDetaylari = ProfileModel.objects.filter(profileSahibi = request.user)
    updateProfile = {}
    profileUptade  = ProfileModel.objects.filter(profileSahibi__id = profileID).first()
    
    if request.method == "POST":
        updateProfile = UpdateProfile(request.POST, request.FILES, instance = profileUptade)
        if updateProfile.is_valid():
            updateProfile.save()
            return redirect('profile',profileID)
        else:
            return redirect('404')
        
    profileQuerySet  = ProfileModel.objects.filter(profileSahibi__id = profileID)

    for profile in profileQuerySet:
        updateProfile[profile.id] = UpdateProfile(instance = profile)
        context["update"]  = updateProfile.items()

    
    return render(request, 'profile.html', context)

