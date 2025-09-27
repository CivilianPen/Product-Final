from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.contrib.admin import widgets
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('main')

class AddPostForm_get(forms.Form):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(AddPostForm_get, self).__init__(*args, **kwargs)
        if self.user:
            # Do something with the user, such as pre-populate a field
            self.fields['username'].initial = self.user.username

    username = forms.Field(disabled=True)
    Request = forms.ModelChoiceField(Goods.objects.all())
    Request_count = forms.IntegerField(validators=[MinValueValidator(1)])

class Admin_AddPostForm_get(forms.ModelForm):
    class Meta:
        model = Applications_get
        fields = ('username', 'Request', 'Request_count', 'Status')
        labels = {
            'username': 'Имя',
            'Request': 'Предет',
            'Request_count': 'Количество',
            'Status': 'Статус',
        }
        widgets ={
            'username': forms.TextInput(attrs={'readonly': 'True'}),
            'Request': forms.TextInput(attrs={'readonly': 'True'}),
            'Request_count': forms.TextInput(attrs={'readonly': 'True'}),
        }

class AddPostForm_repiar(forms.Form):
    CHOICES = {'Ремонт':'Ремонт','Замена':'Замена'}
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(AddPostForm_repiar, self).__init__(*args, **kwargs)
        if self.user:
            # Do something with the user, such as pre-populate a field
            self.fields['username'].initial = self.user.username

    username = forms.Field(disabled=True)
    Request = forms.ModelChoiceField(Goods.objects.all())
    Aim = forms.ChoiceField(choices=CHOICES)
    Comment = forms.CharField(max_length=150)

class Admin_AddPostForm_repiar(forms.ModelForm):
    class Meta:
        model = Applications_repair
        fields = ('username', 'Request', 'Aim','Comment','Status')
        labels = {
            'username': 'Имя',
            'Request': 'Предмет',
            'Aim': 'Действие',
            'Comment': 'Комментарий',
            'Status': 'Статус',
        }
        widgets ={
            'username': forms.TextInput(attrs={'readonly': 'True'}),
            'Request': forms.TextInput(attrs={'readonly': 'True'}),
            'Aim': forms.TextInput(attrs={'readonly': 'True'}),
            'Comment': forms.TextInput(attrs={'readonly': 'True'}),
        }

class AddPostForm(forms.Form):
    login = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class PurchasePlanForm(forms.ModelForm):
    class Meta:
        model = PurchasePlan
        fields = ['item', 'supplier', 'planned_price', 'count', 'planned_date']
        labels = {
            'item': 'Предмет',
            'supplier': 'Поставщик',
            'planned_price': 'Планируемая цена',
            'count': "Количество",
            'planned_date': 'Планируемая дата',
        }
        widgets = {
            'planned_date': forms.TextInput(attrs={'class': 'flatpickr'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        supplier = cleaned_data.get("supplier")
        if not supplier:
            raise forms.ValidationError("Поставщик обязателен.")
        return cleaned_data


class UpdateGoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ('goods', 'count', 'condition')
        labels = {
            'goods': 'Предмет',
            'count': 'Количество',
            'condition': 'Состояние',
        }


class NewGoodsName(forms.ModelForm):
    class Meta:
        model = Goods_Names
        fields = ('name_of_good',)
        labels = {
            'name_of_good': 'Предмет',
        }

class Form_Inventory_management(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('User', 'Rent', 'Count')
        labels = {
            'User': 'Имя',
            'Rent': 'Предмет',
            'Count': 'Количество',
        }
        widgets = {

        }

class HistoryUpdate(forms.ModelForm):
    class Meta:
        model = History
        fields = ('User', 'Rent', 'Count','condition_before','condition_after','rented_at','returned_at')
        labels = {
            'User': 'Имя',
            'Rent': 'Предмет',
            'Count': 'Количество',
            'condition_before' : 'Состояние до',
            'condition_after' : 'Состояние после',
            'rented_at' : 'Когда взято',
            'returned_at' : 'Когда возвращено',
        }
        widgets = {

            'rented_at': forms.TextInput(attrs={'class': 'flatpickr'}),
            'returned_at': forms.TextInput(attrs={'class': 'flatpickr'}),
        }