# Generated by Django 4.1.6 on 2023-02-09 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_alter_ads_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ads',
            name='address',
        ),
    ]