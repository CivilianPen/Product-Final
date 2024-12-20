from django.db import models
from .models import  *
from django.contrib.auth import get_user_model

class Goods(models.Model):
    state = {'новый':'новый','используемый':'используемый','сломанный': 'сломанный'}
    goods = models.CharField('Название',max_length=30)
    count = models.IntegerField('Количество')
    condition = models.CharField('Состояние',max_length=20, choices=state)


    def __str__(self):
        return self.goods

class Applications(models.Model):
    User = models.CharField('ИМЯ',max_length=16)
    Request = models.CharField('ОТЗЫВ',max_length=1600)
