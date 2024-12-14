from django.shortcuts import render
from .models import *
from django.http import HttpResponse
def grounds(request):
    ship = list(Ships.objects.all())
    flatt = list(Flat.objects.all())
    giftt = list(Gifts.objects.all())
    return render(request, 'grounds/grounds.html' , {'ship' : ship , 'flatt': flatt , 'giftt' : giftt})

def win(request):
    return render(request, 'grounds/winnings.html')
