"""This file contains models and schemas to get and work with data received
from a database"""
from django.db import models
from pydantic import BaseModel
# -------------------------------------------------------------------------


class AdsModel(models.Model):
    """This class represents an advertisement model"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    author = models.CharField(max_length=80)
    price = models.IntegerField()
    description = models.CharField(max_length=800, null=True, blank=True)
    address = models.CharField(max_length=80)
    is_published = models.BooleanField(default=False)


class CategoryModel(models.Model):
    """This class represents a category model"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)


class AdsSchema(BaseModel):
    """This class is a schema to serialize and deserialize Ads models"""
    id: int
    name: str
    author: str
    price: int
    description: str
    address: str
    is_published: bool

    class Config:
        orm_mode = True


class CategorySchema(BaseModel):
    """This class is a schema to serialize and deserialize Category models"""
    id: int
    name: str

    class Config:
        orm_mode = True
