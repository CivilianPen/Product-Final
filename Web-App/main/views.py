from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.db.models.signals import post_init
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView

from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .utils import *
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('main')

def page(request):
    ''' Главная страница (просмотр инвентаря)'''
    Items = list(Stations.objects.all())
    urls = Url_adress.objects.all()
    if request.method == 'POST':
        form = URL(request.POST)
        if form.is_valid():
            try:
                Url_adress.objects.create(**form.cleaned_data)
                return redirect('main')
            except:
                form.add_error(None, 'Ошибка')
    else:
        form = URL()

    return render(request, 'main/index.html' , {'Items': Items,'form': form})
