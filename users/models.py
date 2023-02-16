"""This file contains models for user table to get,
create and update data"""
from django.db import models
# -------------------------------------------------------------------------


class User(models.Model):
    """This class represents a user model"""
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    username = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=20, null=True)
    age = models.IntegerField(null=True)
    location = models.ForeignKey('locations.location', on_delete=models.CASCADE,
                                 null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
