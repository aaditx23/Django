from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.zero, name='zero'),
    path('home',views.home, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('index', views.index, name='index')
]