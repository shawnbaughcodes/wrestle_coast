from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
# Create your views here.
def current_user(request):
    if 'user_id' in request.session:
        return User.objects.get(id=request.session['user_id'])
# HELPER FUNCTION END
# INDEX ROUTE
def index(request):
    return render(request, 'login_and_registration/index.html')
# LOGIN FUNCTION
def login(request):
    return render(request, 'login_and_registration/login.html')
    # LOIGGING IN VALIDAITION
def logging_in(request):
    is_valid = User.objects.login_validate(request.POST)
    if is_valid['status'] == True:
        request.session['user_id'] = is_valid['user'].id
        return redirect('/browse')
    else:
        if is_valid['status'] == False:
            messages.error(request, is_valid['message'])
        return redirect('/login')

def register(request):
    return render(request, 'login_and_registration/register.html')

def registration(request):
    is_valid = User.objects.register_validate(request.POST)
    if type(is_valid) == dict:
        for error in is_valid['errors']:
            messages.error(request, error)
        return redirect('/register')
    else:
        user = User.objects.create_user(request.POST)
        request.session['user_id'] = user.id
        return redirect('/browse')

def logout(request):
    request.session.clear()
    return redirect('/')
