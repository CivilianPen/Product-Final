from django.db import models
from .models import  *

# Create your models here.
class Goods(models.Model):
    state = {'новый':'новый','используемый':'используемый','сломанный': 'сломанный'}
    goods = models.CharField('Название',max_length=30)
    count = models.IntegerField('Количество')
    condition = models.CharField('Состояние',max_length=20, choices=state)


    def __str__(self):
        return self.goods