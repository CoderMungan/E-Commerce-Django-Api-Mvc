# Generated by Django 4.2.3 on 2023-08-23 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteApp', '0008_alter_tasarim_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasarim',
            name='fiyat',
            field=models.IntegerField(blank=True, default=0, verbose_name='Fiyat'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tasarim',
            name='image',
            field=models.ImageField(upload_to='siteApp/Uploads', verbose_name='Resim Dosya'),
        ),
    ]
