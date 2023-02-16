"""This file contains models and schemas to work with location table"""
from django.db import models
# ------------------------------------------------------------------------


class Location(models.Model):
    """Location model class for location table"""
    name = models.CharField(max_length=80)
    lat = models.DecimalField(decimal_places=6, max_digits=8, null=True)
    lng = models.DecimalField(decimal_places=6, max_digits=8, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'
