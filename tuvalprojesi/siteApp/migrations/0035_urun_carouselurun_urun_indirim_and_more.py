# Generated by Django 4.2.3 on 2023-09-06 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteApp', '0034_alter_urun_urunaciklama_alter_urun_urunbaslik'),
    ]

    operations = [
        migrations.AddField(
            model_name='urun',
            name='carouselUrun',
            field=models.BooleanField(default=0, verbose_name='Ürün Başa Çıksın mı?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='urun',
            name='indirim',
            field=models.IntegerField(default=1, verbose_name="İndirim Oranı: %'siz yazınız!"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='profileBio',
            field=models.TextField(blank=True, default='', max_length=500, verbose_name='Biografi'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='profileFacebook',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='profileInstagram',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='profileLocation',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Konum'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='profileTwitter',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Twitter'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='profileWebPage',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Web Sayfası'),
        ),
    ]
