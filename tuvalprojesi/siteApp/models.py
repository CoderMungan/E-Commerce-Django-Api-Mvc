from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tasarim(models.Model):

    image = models.ImageField(("Resim Dosya"), upload_to="siteApp/Uploads", height_field=None, width_field=None, max_length=None)
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

