from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('main')

class AddPostFormR(forms.Form):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(AddPostFormR, self).__init__(*args, **kwargs)
        if self.user:
            # Do something with the user, such as pre-populate a field
            self.fields['username'].initial = self.user.username

    username = forms.Field(disabled=True)
    C =(Goods.objects.values_list('count'))
    N = (Goods.objects.values_list('goods'))


    Request = forms.ModelChoiceField(Goods.objects.all())
    Request_count = forms.IntegerField(validators=[MinValueValidator(1)])


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

