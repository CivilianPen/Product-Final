from django.urls import path
from . import views


urlpatterns = [
    path('', views.grounds),
    path('winning', views.win),
]