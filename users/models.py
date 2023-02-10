"""This file contains models and schemas for user and location tables to get,
create and update data"""
from typing import Any
from django.db import models
from pydantic import BaseModel, validator
# -------------------------------------------------------------------------


class Location(models.Model):
    """Location model class for location table"""
    name = models.CharField(max_length=80, null=True)
    lat = models.DecimalField(decimal_places=6, max_digits=8, null=True)
    lng = models.DecimalField(decimal_places=6, max_digits=8, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class User(models.Model):
    """This class represents a user model"""
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    username = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=20, null=True)
    age = models.IntegerField(null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class UserSchema(BaseModel):
    """The UserSchema class serves to serialize and deserialize user models"""
    first_name: str = None
    last_name: str = None
    username: str
    password: str
    role: str = 'member'
    age: int = None
    location: Any = None

    @validator('location')
    def validate(cls, value: Any) -> str:
        """This method validates the value of the location field and provides
        an appropriate type of the field if the value is not a string"""
        if isinstance(value, Location):
            return str(value.name)

        elif type(value) is list:
            return ', '.join(value)

        else:
            return value

    class Config:
        orm_mode = True


class LocationSchema(BaseModel):
    """The LocationSchema class serves to serialize and deserialize location
    models"""
    name: str | list = None
    lat: float = None
    lng: float = None

    class Config:
        orm_mode = True
