# Generated by Django 4.2.3 on 2023-08-27 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteApp', '0021_remove_yorumyap_yorumyapankisi'),
    ]

    operations = [
        migrations.AddField(
            model_name='yorumyap',
            name='yorumAtCrated',
            field=models.DateTimeField(auto_now=True, verbose_name='Yorumun Yapıldığı Zaman'),
        ),
    ]