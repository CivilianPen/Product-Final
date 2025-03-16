from django.db import models
from .models import *
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.utils.crypto import *
import random
import string

class Stations(models.Model):
    data = models.CharField('карта', max_length=10**10, null=True)
    coords = models.CharField('координаты', max_length=10**10, null=True)


    class Meta:
        verbose_name = "Карта"
        verbose_name_plural = "Карты"


class Url_adress(models.Model):
    url = models.CharField(max_length=255)
    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"
