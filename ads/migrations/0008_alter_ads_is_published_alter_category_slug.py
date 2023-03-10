# Generated by Django 4.1.6 on 2023-03-02 16:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0007_category_slug_alter_ads_is_published_alter_ads_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='is_published',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.MaxLengthValidator(10)]),
        ),
    ]
