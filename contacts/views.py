from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Welcome back dear amir!')    

def show():
    pass