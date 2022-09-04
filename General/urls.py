from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.generalpage, name='generalpage'),
    path('login', views.login, name='login')
]
