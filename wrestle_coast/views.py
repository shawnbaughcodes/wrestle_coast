from django.shortcuts import render
from .models import *
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'wrestle_coast/index.html')

def register(request):
    return render(request, 'wrestle_coast/register.html')

def login(request):
    return render(request, 'wrestle_coast/login.html')
