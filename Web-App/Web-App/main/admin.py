from django.contrib import admin
from .models import  *

# Register your models here.
@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['goods','count','condition']
    list_editable = ['goods','count','condition']
    list_display_links = None

@admin.register(Applications)
class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ['User','Request']
    list_editable = ['User','Request']
    list_display_links = None