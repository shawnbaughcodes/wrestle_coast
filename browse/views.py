from django.shortcuts import render, redirect
import os
from login_and_registration.models import User

def current_user(request):
    if 'user_id' in request.session:
        return User.objects.get(id=request.session['user_id'])
# Create your views here.
def index(request):
    context = {
    'user' : current_user(request),
    }
    return render(request, 'browse/index.html', context)

def admin(request):
    return redirect('/company')

def logout(request):
    request.session.clear()
    return redirect('/')
