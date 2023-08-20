from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tasarim(models.Model):

    image = models.ImageField(("Resim Dosya"), upload_to="Resimler", height_field=None, width_field=None, max_length=None)
    sanatci = models.ForeignKey(User, verbose_name=("Sanatci"), on_delete=models.CASCADE)
    sanatEseri = models.TextField(("Sanat Eseri İçeriği"), max_length=500)
    createdAt = models.DateTimeField(("Oluşturulma Tarihi"), auto_now=True)

