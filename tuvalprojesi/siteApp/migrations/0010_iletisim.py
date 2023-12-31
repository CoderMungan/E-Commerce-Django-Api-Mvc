# Generated by Django 4.2.3 on 2023-08-24 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteApp', '0009_tasarim_fiyat_alter_tasarim_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iletisim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='İsmi')),
                ('email', models.CharField(max_length=150, verbose_name='Email Adresi')),
                ('mesajKonusu', models.CharField(max_length=200, verbose_name='Mesajın Konusu')),
                ('mesajinIcerigi', models.TextField(max_length=500, verbose_name='Mesajın İçeriği')),
            ],
        ),
    ]
