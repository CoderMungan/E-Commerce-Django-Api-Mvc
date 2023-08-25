# Generated by Django 4.2.3 on 2023-08-25 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteApp', '0017_yorumyap'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yorumyap',
            name='yorumSahibininAdı',
        ),
        migrations.AddField(
            model_name='yorumyap',
            name='yorumyapanKisi',
            field=models.CharField(default=0, max_length=50, verbose_name='Yorum Sahibi'),
            preserve_default=False,
        ),
    ]
