# Generated by Django 4.2.3 on 2023-08-24 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteApp', '0015_remove_yorum_yorumsahibi'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Yorum',
        ),
    ]