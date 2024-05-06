from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    return render(request, 'home.html')

def inicio(request):
    return render(request, "inicio.html")