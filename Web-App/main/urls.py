from django.urls import path
from . import views
from .views import *
from django.contrib import admin

urlpatterns = [
    path('', views.page, name="main"),
    path('my', views.page2, name="my"),
    path('application-get', views.ApplicationsForm, name='application-get'),
    path('application-repair', views.ApplicationsForm2, name='application-repair'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name="login"),
    path('logout', logout_user, name="logout"),
    path('console',views.AdminPage, name = 'console'),
    path('console/purchase-plan/', views.purchase_plan, name='purchase_plan'),
    path('console/delete-purchase-plan/<int:post_id>/', views.delete_purchase_plan, name='delete_purchase_plan'),
    path('console/edit-inventory/', views.edit_inventory, name='edit_inventory'),
    path('console/new-name-inventory/', views.new_name_inventory, name='new_name_inventory'),
    path('console/update-name-inventory/<int:post_id>/', views.update_name_inventory, name='update_name_inventory'),
    path('console/delete-name-inventory/<int:post_id>/', views.delete_name_inventory, name='delete_name_inventory'),
    path('console/update-inventory/<int:post_id>/', views.Update_inventory, name="Update_inventory"),
    path('console/delete-inventory/<int:post_id>/', views.Delete_inventory, name="Delete_inventory"),
    path('console/request-for-receipt-inventory/', views.Request_for_receipt_inventory, name="Request_for_receipt_inventory"),
    path('console/request-for-receipt-inventory-update/<int:post_id>/', views.Update_Request_for_receipt_inventory, name="Update_application_get"),
    path('console/request-for-receipt-inventory-delete/<int:post_id>/', views.Delete_Request_for_receipt_inventory, name="Delete_application_get"),
    path('console/request-for-repair-inventory/', views.Request_for_repair_inventory, name="Request_for_repair_inventory"),
    path('console/request-for-repair-inventory-delete/<int:post_id>/', views.Delete_Request_for_repair_inventory, name="Delete_Request_for_repair_inventory"),
    path('console/request-for-repair-inventory-update/<int:post_id>/', views.Update_Request_for_repair_inventory, name="Update_Request_for_repair_inventory"),
    path('console/inventory-management/', views.Inventory_management, name="Inventory_management"),
    path('console/inventory-management-delete/<int:post_id>/', views.Inventory_management_delete, name="Inventory_management_delete"),
    path('console/history/', views.history, name="history"),
    path('console/history-update/<int:post_id>/', views.Update_history, name="Update_history"),
    path('console/history-delete/<int:post_id>/', views.Delete_history, name="Delete_history"),

]