from django.db import models
from .models import  *
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
class Goods(models.Model):
    state = {'новый':'новый','используемый':'используемый','сломанный': 'сломанный'}
    goods = models.CharField('Название',max_length=30)
    count = models.IntegerField('Количество')
    condition = models.CharField('Состояние',max_length=20, choices=state)


    def __str__(self):
        return self.goods

class Applications(models.Model):
    state = {'На рассмотрении': 'На рассмотрении', 'Одобрено': 'Одобрено', 'Отказано': 'Отказано'}
    username = models.CharField(max_length=100)
    Request = models.ForeignKey('Goods' ,on_delete=models.PROTECT,null=True)
    Request_count = models.PositiveIntegerField('count',default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    Status = models.CharField('Статус заявки',default='На рассмотрении', choices=state,max_length=100)

