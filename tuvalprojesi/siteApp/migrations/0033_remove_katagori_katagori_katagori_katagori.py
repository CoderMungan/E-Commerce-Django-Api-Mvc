# Generated by Django 4.2.3 on 2023-09-04 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteApp', '0032_urun_kategori'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='katagori',
            name='katagori',
        ),
        migrations.AddField(
            model_name='katagori',
            name='katagori',
            field=models.CharField(default=0, max_length=50, verbose_name='Kategoriler'),
            preserve_default=False,
        ),
    ]
