import imp
from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show, name= 'show'),
    path('insert', views.insert, name= 'insert'),
    path('show', views.show, name='show'),
]
