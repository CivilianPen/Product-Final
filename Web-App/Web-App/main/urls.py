from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.page, name="main"),
    path('page', views.addpage),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name="login"),
    path('logout', logout_user, name="logout")
]