from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Katagori(models.Model):
    katagori = models.CharField(("Kategoriler"), max_length=50)

    def __str__(self) -> str:
        return self.katagori

class Urun(models.Model):
    image = models.ImageField(("Ürünün Resmi"), upload_to="", height_field=None, width_field=None, max_length=None)
    image2 = models.ImageField(("Ürünün 2. Resmi"), upload_to="", height_field=None, width_field=None, max_length=None)
    image3 = models.ImageField(("Ürünün 3. Resmi"), upload_to="", height_field=None, width_field=None, max_length=None, blank=True)
    image4 = models.ImageField(("Ürünün 4. Resmi"), upload_to="", height_field=None, width_field=None, max_length=None,blank=True)
    image5 = models.ImageField(("Ürünün 5. Resmi"), upload_to="", height_field=None, width_field=None, max_length=None,blank=True)
    fiyat = models.IntegerField(("Fiyat"), blank=True)
    eskiFiyat = models.IntegerField(("Eski Fiyat"), blank=True)
    kategori = models.ForeignKey(Katagori, verbose_name=("Ürün Kategorisi"), on_delete=models.CASCADE, blank=False)
    urunBaslik = models.CharField(("Ürün Başlık"), max_length=500)
    urunAciklama = models.TextField(("Ürün Açıklaması"), max_length=500)
    urunDetayAciklama = models.TextField(("Ürün Detay Açıklaması"), max_length=1500)
    createdAt = models.DateTimeField(("Oluşturulma Tarihi"), auto_now=True)
    urunBegenme = models.BooleanField(("Beğenme"), default=False ,blank=True)
    carouselUrun = models.BooleanField(("Ürün Anasayfaya Çıksın mı?"), default=False , blank=True)
    carouselFavori = models.BooleanField(("Sayfada İlk Çıkacak Ürün mü? DipNot: Bir tane seçilebilir!"), default=False , blank=True)
    indirim = models.IntegerField(("İndirim Oranı: %'siz yazınız!"), default=0, blank=True)


    def __str__(self) -> str:
        return self.urunBaslik
    

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

    urun = models.ForeignKey(Urun, verbose_name=("Ürün Adı"), on_delete=models.CASCADE)
    yorumSahibi = models.ForeignKey(User, verbose_name=("Yorun sahibi"), on_delete=models.CASCADE)
    yorumBaslik = models.CharField(("Yorumun Başlığı"), max_length=100)
    yorumIcerik = models.TextField(("Yorum İçeriği"), max_length=500)
    yorumAtCrated = models.DateTimeField(("Yorumun Yapıldığı Zaman"), auto_now=True)


    def __str__(self) -> str:
        return self.yorumBaslik
    
class ProfileModel(models.Model):

    profileSahibi = models.ForeignKey(User, verbose_name=("Profil Sahibi"), on_delete=models.CASCADE)
    profileAvatar = models.ImageField(("Avatar"), upload_to="", height_field=None, default="/Uploads/Avatar.png", width_field=None, max_length=None, blank=True)
    profileBio = models.TextField(("Biografi"), max_length=500, default="", blank=True)
    profileLocation = models.CharField(("Konum"), max_length=150, default="" , blank=True)
    profileInstagram = models.CharField(("Instagram"), max_length=150, default="", blank=True)
    profileTwitter = models.CharField(("Twitter"), max_length=150, default="", blank=True)
    profileFacebook = models.CharField(("Facebook"), max_length=150, default="", blank=True)
    profileWebPage = models.CharField(("Web Sayfası"), max_length=150, default="", blank=True)


    def __str__(self) -> str:
        return self.profileSahibi.username