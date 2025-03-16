from django.contrib import admin
from .models import  *


# Register your models here.


@admin.register(Stations)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['data','coords']
    list_editable = ['data','coords']
    list_display_links = None

@admin.register(Url_adress)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['url']
    list_editable = ['url']
    list_display_links = None

