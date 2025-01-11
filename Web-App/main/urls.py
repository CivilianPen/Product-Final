from django.urls import path
from . import views
from .views import *
from django.contrib import admin

urlpatterns = [
    path('', views.page, name="main"),
    path('application', views.ApplicationsForm, name='application'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name="login"),
    path('logout', logout_user, name="logout"),
    path('console',views.AdminPage, name = 'console'),
    path('console/add-purchase-plan/', views.add_purchase_plan, name='add_purchase_plan'),
    path('console/purchase-plans/', views.purchase_plan_list, name='purchase_plan_list'),
]