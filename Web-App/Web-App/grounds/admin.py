from django.contrib import admin

#Register your models here.
from .models import  *




@admin.register(Ships)
class ShipsAdmin(admin.ModelAdmin):
    list_display = ['X','Y','gift','flat']
    list_editable = ['X', 'Y','gift','flat']
    list_display_links = None


@admin.register(Gifts)
class GiftsAdmin(admin.ModelAdmin):
    list_display = ['title','description']
    list_editable = ['title','description']
    list_display_links = None

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ['Size','Ammo','user']
    list_editable = ['Size','Ammo','user']
    list_display_links = None

