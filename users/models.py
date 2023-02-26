"""This file contains models for user table to get,
create and update data"""
from django.contrib.auth.models import AbstractUser
from django.db import models
# -------------------------------------------------------------------------


class User(AbstractUser):
    """This class represents a user model"""
    MEMBER = 'member'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    ROLES = [(MEMBER, MEMBER), (MODERATOR, MODERATOR), (ADMIN, ADMIN)]
    role = models.CharField(max_length=9, choices=ROLES)
    age = models.IntegerField(null=True)
    location = models.ForeignKey('locations.location', on_delete=models.CASCADE,
                                 null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
