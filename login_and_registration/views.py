from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.
# INDEX ROUTE
def index(request):
    return render(request, 'login_and_registration/index.html')

def login(request):
    return render(request, 'login_and_registration/login.html')

def logging_in(request):
    return redirect('/login')

def register(request):
    return render(request, 'login_and_registration/register.html')

def registration(request):
    return redirect('/register')
