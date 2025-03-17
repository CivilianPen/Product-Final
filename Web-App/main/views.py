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
import requests
def parsing(url):
    tiles = []
    s = []
    for i in range(52):
        response = requests.get(url)
        data = response.json()['message']['data']
        if not data in tiles:
            tiles.append(data)
    order = [[-1] * 4, [-1] * 4, [-1] * 4, [-1] * 4]
    c = 0
    for x in range(4):
        for y in range(4):
            for i in range(16):
                c = 0
                for j in range(64):
                    if x == 0 and y == 0:
                        if tiles[i][0][j] == 255 and tiles[i][j][0] == 255:
                            c += 1
                    elif x == 0:
                        if abs(tiles[i][0][j] - tiles[order[y - 1][x]][63][j]) <= 5 and tiles[i][j][0] == 255:
                            c += 1
                    elif y == 0:
                        if tiles[i][0][j] == 255 and abs(tiles[i][j][0] - tiles[order[y][x - 1]][j][63]) <= 5:
                            c += 1
                    else:
                        if abs(tiles[i][0][j] - tiles[order[y - 1][x]][63][j]) <= 5 and abs(
                                tiles[i][j][0] - tiles[order[y][x - 1]][j][63]) <= 5:
                            c += 1
                if c >= 55:
                    order[y][x] = i
    for x in range(4):
        for y in range(4):
            order[x][y] = tiles[order[x][y]]
    a = []
    for i in range(256):
        a.append([0])
        for j in range(256):
            a[i].append([0])
            a[i][j] = order[i // 64][j // 64][i % 64][j % 64]
    return a
def parsing2(url):
    response = requests.get(url+'/coords')
    data = response.json()['message']
    return data

def page(request):
    ''' Главная страница (просмотр инвентаря)'''
    Items = list(Stations.objects.all())
    urls = Url_adress.objects.all()
    if request.method == 'POST':
        form = URL(request.POST)
        if form.is_valid():

            Url_adress.objects.create(**form.cleaned_data)
            data = parsing(**form.cleaned_data)
            coords = parsing2(**form.cleaned_data)
            С = Stations(data=str(data),coords=str(coords))
            С.save()

            return render(request, 'main/index.html', {'data': data,'coords':coords})

    else:
        form = URL()

    return render(request, 'main/index.html' , {'Items': Items,'form': form})
