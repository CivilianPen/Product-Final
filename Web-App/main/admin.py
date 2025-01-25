from django.contrib import admin
from .models import  *


# Register your models here.
@admin.register(Goods_Names)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['name_of_good']
    list_editable = ['name_of_good']
    list_display_links = None

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['goods','count','rented_count','condition','created_at','updated_at']
    list_editable = ['goods','count','rented_count','condition']
    list_display_links = None

@admin.register(Applications_get)
class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ['username','Request','Request_count','Status']
    list_editable = ['Request','Request_count','Status']
    list_display_links = None

@admin.register(Applications_repair)
class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ['username','Request','Comment','Status']
    list_editable = ['Request','Comment','Status']
    list_display_links = None

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['User','Rent','Count']
    list_editable = ['Rent','Count']
    list_display_links = None


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(PurchasePlan)
class PurchasePlanAdmin(admin.ModelAdmin):
    list_display = ('item', 'supplier', 'planned_price', 'planned_date')

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ['User','Rent','Count','condition_before','condition_after','rented_at','returned_at']
    list_editable = ['Rent','Count','condition_before','condition_after',]
    list_display_links = None