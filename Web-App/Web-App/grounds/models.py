from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.

class Ships(models.Model):
    X = models.IntegerField('X')
    Y = models.IntegerField('Y')
    #gift = models.PositiveSmallIntegerField(('приз'), choices=GIFTS)
    #flat = models.PositiveSmallIntegerField(('поле'), choices=FLATS)
    flat = models.ForeignKey('Flat', on_delete=models.PROTECT,null=True)
    gift = models.ForeignKey('Gifts', on_delete=models.PROTECT, null=True)

    def get_absolute_url(self):
        return reverse('post' , kwargs={'post id': self.pk})


class Gifts(models.Model):
    title = models.CharField('Приз', max_length=30)
    description = models.CharField('Описание', max_length=30)

    def get_absolute_url(self):
        return reverse('Gifts' , kwargs={'Gifts title': self.pk})

    def __str__(self):
        return self.title
class Flat(models.Model):
    Size = models.IntegerField('Размер')
    Ammo = models.IntegerField('Выстрелы' , default='2')
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='scores',
    )
    def get_absolute_url(self):
        return reverse('Flat', kwargs={'Flat id': self.pk})




class forForm(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

