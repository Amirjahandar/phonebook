from django.urls import path
from . import views

urlpatterns = [
    path('', views.show, name= 'show'),
    path('insert', views.insert, name= 'insert'),

]
