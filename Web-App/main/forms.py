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

class URL(forms.Form):
    url = forms.CharField(max_length=255)