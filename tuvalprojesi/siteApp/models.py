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
    hakkimizdaIcerik = models.TextField(("İçerik"), max_length=600)

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

    yorumSahibininAdı = models.ForeignKey(User, verbose_name=("Yorum Sahibi"), on_delete=models.CASCADE, blank=True)
    yorumBaslik = models.CharField(("Yorumun Başlığı"), max_length=100)
    yorumIcerik = models.TextField(("Yorum İçeriği"), max_length=500)

    def __str__(self) -> str:
        return self.yorumBaslik
