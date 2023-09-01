from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tasarim(models.Model):

    image = models.ImageField(("Resim Dosya"), upload_to="", height_field=None, width_field=None, max_length=None)
    fiyat = models.IntegerField(("Fiyat"), blank=True)
    sanatci = models.ForeignKey(User, verbose_name=("Sanatci"), on_delete=models.CASCADE)
    sanatEseriBaslik = models.CharField(("Sanat Eseri Başlığı"), max_length=500)
    sanatEseriAciklamasi = models.TextField(("Sanat Eseri İçeriği"), max_length=500)
    createdAt = models.DateTimeField(("Oluşturulma Tarihi"), auto_now=True)


    def __str__(self) -> str:
        return self.sanatEseriBaslik
    

class Hakkimizda(models.Model):

    hakkimizdaBaslik = models.CharField(("Başlık"), max_length=50)
    hakkimizdaIcerik = models.TextField(("İçerik"), max_length=2000)

    def __str__(self) -> str:
        return self.hakkimizdaBaslik
    

class Iletisim(models.Model):

    name = models.CharField(("İsmi"), max_length=50)
    email = models.CharField(("Email Adresi"), max_length=150)
    mesajKonusu = models.CharField(("Mesajın Konusu"), max_length=200)
    mesajinIcerigi = models.TextField(("Mesajın İçeriği"), max_length=500)

    def __str__(self) -> str:
        return self.mesajKonusu
    

class YorumYap(models.Model):

    urun = models.ForeignKey(Tasarim, verbose_name=("Ürün Adı"), on_delete=models.CASCADE)
    yorumSahibi = models.ForeignKey(User, verbose_name=("Yorun sahibi"), on_delete=models.CASCADE)
    yorumBaslik = models.CharField(("Yorumun Başlığı"), max_length=100)
    yorumIcerik = models.TextField(("Yorum İçeriği"), max_length=500)
    yorumAtCrated = models.DateTimeField(("Yorumun Yapıldığı Zaman"), auto_now=True)


    def __str__(self) -> str:
        return self.yorumBaslik
    
class ProfileModel(models.Model):

    profileSahibi = models.ForeignKey(User, verbose_name=("Profil Sahibi"), on_delete=models.CASCADE)
    profileAvatar = models.ImageField(("Avatar"), upload_to="", height_field=None, default="/Uploads/Avatar.png", width_field=None, max_length=None, blank=True)
    profileBio = models.TextField(("Biografi"), max_length=500, blank=True)
    profileLocation = models.CharField(("Konum"), max_length=150, blank=True)
    profileInstagram = models.CharField(("Instagram"), max_length=150, blank=True)
    profileTwitter = models.CharField(("Twitter"), max_length=150, blank=True)
    profileFacebook = models.CharField(("Facebook"), max_length=150, blank=True)
    profileWebPage = models.CharField(("Web Sayfası"), max_length=150, blank=True)


    def __str__(self) -> str:
        return self.profileBio