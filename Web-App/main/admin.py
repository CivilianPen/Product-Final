from django.contrib import admin
from .models import  *


# Register your models here.


@admin.register(Stations)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['goods','count','rented_count']
    list_editable = ['goods','count','rented_count']
    list_display_links = None

