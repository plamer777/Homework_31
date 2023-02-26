"""This unit contains models to interact with database tables"""
from django.db import models
from ads.models import Ads
from users.models import User
# -------------------------------------------------------------------------


class Selection(models.Model):
    """The Selection class represents advertisement's selection"""
    id = models.AutoField(models.IntegerField, primary_key=True)
    name = models.CharField(max_length=30, null=True)
    items = models.ManyToManyField(Ads)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

