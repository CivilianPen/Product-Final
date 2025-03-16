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
    goods = models.CharField('Состояние', max_length=20, null=True)
    count = models.IntegerField('Количество', default=1,validators=[MinValueValidator(1)])
    rented_count = models.IntegerField('Взято', default=0,validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = "Инвентарь"
        verbose_name_plural = "Инвентарь"

    def __str__(self):
        return f"{self.count-self.rented_count}шт"

class Url_adress(models.Model):
    url = models.CharField(max_length=255)
    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"
