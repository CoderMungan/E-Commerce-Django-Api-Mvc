from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Tasarim, Hakkimizda, Iletisim, YorumYap, ProfileModel

# djangonun user modelini dahil et
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout 


from .form import *

# Create your views here.
def index(request):

    context = {}
    urunler = Tasarim.objects.all()
    context['urunler'] = urunler

    # Arama post geçiliyor

    return render(request, 'index.html', context)

def searchBar(request):

    context = {}

    if request.method == 'POST':
        arama = request.POST.get('search')
        # Post geldiyse ve boş değil ise
        print("index fn:", arama)
        if arama:
            searchUrun = Tasarim.objects.filter(Q(sanatEseriBaslik__icontains = arama)).all()   
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
    
    context['kullanicilar'] = userFilter

    yorumlar = YorumYap.objects.filter(yorumSahibi__id = profileID).all()

    context['yorumlar'] = yorumlar

    profileFront = ProfileModel.objects.filter(profileSahibi__id = profileID).all()

    context['profiller'] = profileFront

    if request.method == 'POST':
        resim = request.POST.get('avatar')
        biografi = request.POST.get('biografi')
        instagram = request.POST.get('instagram')
        twitter = request.POST.get('twitter')
        facebook = request.POST.get('facebook')
        webpage = request.POST.get('webpage')
        location = request.POST.get('konum')
        ProfileModel.objects.create(profileSahibi = request.user, profileAvatar = resim, profileBio = biografi, profileLocation= location, profileInstagram = instagram, profileTwitter = twitter, profileFacebook = facebook, profileWebPage = webpage)
        return redirect('profile', profileID)
    
    # Tüm profilleri al


    # Update yapmaya çalışıyorum
    # profileDetaylari = ProfileModel.objects.filter(profileSahibi = request.user)
    # updateProfile = {}
    
    # for profile in profileDetaylari:
    #     updateProfile[profile.id] = UpdateProfile(instance = profile)
    #     context["update"]  = updateProfile.items()

    
    return render(request, 'profile.html', context)


def deleteurun(request,urunDetayiid):

    deleted=Tasarim.objects.filter(id=urunDetayiid).first()

    if request.user.is_authenticated and request.user.is_superuser:

        deleted.delete()
        return redirect('urun')
    
    else:
        return redirect('404')