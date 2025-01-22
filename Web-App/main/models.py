from django.db import models
from .models import *
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.utils.crypto import *
import random
import string

class Goods(models.Model):
    CONDITION_CHOICES = [
        ('новый', 'новый'),
        ('использованный', 'использованный'),
        ('сломанный', 'сломанный'),
    ]

    goods = models.CharField('Название', max_length=30)
    count = models.IntegerField('Количество', default=0)
    rented_count = models.IntegerField('Взято', default=0)
    condition = models.CharField('Состояние', max_length=20, choices=CONDITION_CHOICES)
    description = models.TextField('Описание', blank=True, null=True)
    created_at = models.DateTimeField('Добавлено', default=timezone.now)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)


    class Meta:
        verbose_name = "Инвентарь"
        verbose_name_plural = "Инвентарь"

    def __str__(self):
        return self.goods

    def get_absolute_url(self):
        return reverse("Update_inventory", kwargs={"post_id": self.id})
    def get_absolute_url_del(self):
        return reverse("Delete_inventory", kwargs={"post_id": self.id})
    def available_count(self):
        """Возвращает количество доступных к использованию предметов."""
        return self.count - self.rented_count

    def is_available(self):
        """Проверяет, есть ли доступные предметы."""
        return self.available_count() > 0

    def rent_item(self, quantity=1):
        """
        Уменьшает доступное количество предметов при аренде.
        :param quantity: Количество предметов, которое нужно взять.
        :return: True, если операция успешна; False, если недостаточно предметов.
        """
        if self.available_count() >= quantity:
            self.rented_count += quantity
            self.save()
            return True
        return False

    def return_item(self, quantity=1):
        """
        Увеличивает доступное количество предметов при возврате.
        :param quantity: Количество предметов, которое нужно вернуть.
        """
        if self.rented_count >= quantity:
            self.rented_count -= quantity
            self.save()


class Applications_get(models.Model):
    state = {'На рассмотрении': 'На рассмотрении', 'Одобрено': 'Одобрено', 'Отказано': 'Отказано'}
    username = models.CharField('Имя',max_length=100)
    Request = models.ForeignKey('Goods' ,on_delete=models.PROTECT,null=True,verbose_name='Предмет')
    Request_count = models.PositiveIntegerField('Количество',default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    Status = models.CharField('Статус заявки',default='На рассмотрении', choices=state,max_length=100)

    class Meta:
        verbose_name = "Заявка на получение"
        verbose_name_plural  = "Заявки на получение"

    def get_absolute_url(self):
        return reverse("Update_application_get", kwargs={"post_id": self.id})
    def get_absolute_url_del(self):
        return reverse("Delete_application_get", kwargs={"post_id": self.id})

    def get_absolute_url_give(self):
        return reverse("Give_inventory", kwargs={"post_id": self.id})
    def get_absolute_url_return(self):
        return reverse("Return_inventory", kwargs={"post_id": self.id})


class Applications_repair(models.Model):
    CHOICES = {'Ремонт': 'Ремонт', 'Замена': 'Замена'}
    state = {'На рассмотрении': 'На рассмотрении', 'Выполнено': 'Выполнено', 'Отказано': 'Отказано'}
    username = models.CharField('Имя',max_length=100)
    Request = models.ForeignKey('Goods' ,on_delete=models.PROTECT,null=True,verbose_name='Предмет')
    Aim = models.CharField('Действие',choices=CHOICES,default='Ремонт',max_length=100)
    Comment = models.CharField('Комментарий', max_length=150)
    Status = models.CharField('Статус заявки',default='На рассмотрении', choices=state,max_length=100)

    class Meta:
        verbose_name = "Заявка на ремонт"
        verbose_name_plural  = "Заявки на ремонт"

    def get_absolute_url(self):
        return reverse("Update_Request_for_repair_inventory", kwargs={"post_id": self.id})
    def get_absolute_url_del(self):
        return reverse("Delete_Request_for_repair_inventory", kwargs={"post_id": self.id})
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
