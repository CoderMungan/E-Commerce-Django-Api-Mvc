# Generated by Django 4.2.3 on 2023-09-09 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteApp', '0044_alter_urun_urundetayaciklama'),
    ]

    operations = [
        migrations.AddField(
            model_name='yorumyap',
            name='yorumProfile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='siteApp.profilemodel', verbose_name='Profil'),
            preserve_default=False,
        ),
    ]
