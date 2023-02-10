"""This file contains models and schemas to get and work with data received
from a database"""
from typing import Any, Optional
from django.db.models.fields.files import ImageFieldFile
from users.models import User
from django.db import models
from pydantic import BaseModel, validator
# -------------------------------------------------------------------------


class Category(models.Model):
    """This class represents a category model"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Ads(models.Model):
    """This class represents an advertisement model"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.CharField(max_length=800, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class AdsSchema(BaseModel):
    """This class is a schema to serialize and deserialize Ads models"""
    name: str = None
    author_id: int
    price: int
    image: Any
    description: str = None
    is_published: bool = False
    category_id: int

    @validator('image')
    def validate(cls, value: Any) -> Optional[str]:
        """This method serves to validate the given value and if it is not
        valid to return appropriate value's type"""
        if value and isinstance(value, ImageFieldFile):
            return value.url

        elif type(value) is str:
            return value

        return None

    class Config:
        orm_mode = True


class CategorySchema(BaseModel):
    """This class is a schema to serialize and deserialize Category models"""
    name: str

    class Config:
        orm_mode = True
