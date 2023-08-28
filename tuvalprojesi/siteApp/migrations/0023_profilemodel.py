# Generated by Django 4.2.3 on 2023-08-28 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('siteApp', '0022_yorumyap_yorumatcrated'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profileAvatar', models.ImageField(upload_to='', verbose_name='Avatar')),
                ('profileBio', models.TextField(max_length=500, verbose_name='Biografi')),
                ('profileSahibi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Profil Sahibi')),
            ],
        ),
    ]