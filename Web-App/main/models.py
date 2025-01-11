from django.db import models
from .models import  *
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator


class Goods(models.Model):
    state = {'новый':'новый','используемый':'используемый','сломанный': 'сломанный'}
    goods = models.CharField('Название',max_length=30)
    count = models.IntegerField('Количество')
    rented_count = models.IntegerField('Взято',default=0)
    condition = models.CharField('Состояние',max_length=20, choices=state)

    class Meta:
        verbose_name = "Инвентарь"
        verbose_name_plural  = "Инвентарь"

    def __str__(self):
        return self.goods

class Applications_get(models.Model):
    state = {'На рассмотрении': 'На рассмотрении', 'Одобрено': 'Одобрено', 'Отказано': 'Отказано'}
    username = models.CharField('Имя',max_length=100)
    Request = models.ForeignKey('Goods' ,on_delete=models.PROTECT,null=True,verbose_name='Предмет')
    Request_count = models.PositiveIntegerField('Количество',default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    Status = models.CharField('Статус заявки',default='На рассмотрении', choices=state,max_length=100)

    class Meta:
        verbose_name = "Заявка на получение"
        verbose_name_plural  = "Заявки на получение"

class Applications_repair(models.Model):
    state = {'На рассмотрении': 'На рассмотрении', 'Выполнено': 'Выполнено', 'Отказано': 'Отказано'}
    username = models.CharField('Имя',max_length=100)
    Request = models.ForeignKey('Goods' ,on_delete=models.PROTECT,null=True,verbose_name='Предмет')
    Comment = models.CharField('Комментарий', max_length=150)
    Status = models.CharField('Статус заявки',default='На рассмотрении', choices=state,max_length=100)

    class Meta:
        verbose_name = "Заявка на ремонт"
        verbose_name_plural  = "Заявки на ремонт"

class Users(models.Model):
    User = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='scores',
    )
    Rent = models.ForeignKey('Goods', on_delete=models.PROTECT, null=True,blank=True)
    Count = models.IntegerField('Количество',default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    Plus = models.BooleanField(default=False,editable=False)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural  = "Пользователи"

class Supplier(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Поставщик")

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

    def __str__(self):
        return self.name


class PurchasePlan(models.Model):
    item = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='purchase_plans', verbose_name="Товар")
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, verbose_name="Поставщик")
    planned_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Планируемая цена")
    count = models.PositiveIntegerField(default=1, verbose_name="Количество")
    planned_date = models.DateField(verbose_name="Планируемая дата")

    class Meta:
        verbose_name = "План закупки"
        verbose_name_plural = "Планы закупок"

    def __str__(self):
        return f"{self.count} {self.item.goods} from {self.supplier.name} at {self.planned_price} on {self.planned_date}"
