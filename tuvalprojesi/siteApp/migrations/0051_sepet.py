# Generated by Django 4.2.3 on 2023-09-09 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('siteApp', '0050_alter_profilemodel_profileavatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sepet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sepeteAtilma', models.BooleanField(default=False, verbose_name='Sepette')),
                ('adet', models.PositiveIntegerField(blank=True, default=0, verbose_name='Kaç Adet')),
                ('urun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteApp.urun', verbose_name='Ürün')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
    ]