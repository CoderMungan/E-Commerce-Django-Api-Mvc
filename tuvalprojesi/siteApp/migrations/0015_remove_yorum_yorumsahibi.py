# Generated by Django 4.2.3 on 2023-08-24 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteApp', '0014_yorum_yorumsahibi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yorum',
            name='yorumSahibi',
        ),
    ]
