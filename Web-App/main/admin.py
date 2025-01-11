from django.contrib import admin
from .models import  *


# Register your models here.
@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['goods','count','rented_count','condition']
    list_editable = ['goods','count','rented_count','condition']
    list_display_links = None

@admin.register(Applications)
class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ['username','Request','Request_count','Status']
    list_editable = ['Request','Request_count','Status']
    list_display_links = None


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['User','Rent','Count','Plus']
    list_editable = ['Rent','Count']
    list_display_links = None


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(PurchasePlan)
class PurchasePlanAdmin(admin.ModelAdmin):
    list_display = ('item', 'supplier', 'planned_price', 'planned_date')