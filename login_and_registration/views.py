from django.shortcuts import render
from .models import *
from django.contrib import messages
# Create your views here.
def register(request):
    return render(request, 'wrestle_coast/register.html')
# START REGISTRATION
def registration(request):
    is_valid = User.objects.register_validate(request.POST)
    if type(is_valid) == dict:
        for error in is_valid['errors']:
            messages.error(request, error)
            return redirect('/register')
    else:
        user = User.objects.create_user(request.POST)
        request.session['user_id'] = user.id
        return redirect('/home')
# END ALL REGISTER FUNCTIONS******
# START LOGIN RENDER
def login(request):
    return render(request, 'wrestle_coast/login.html')
# START LOGGING IN
def logging_in(request):
    is_valid = User.objects.login_validate(request.POST)
    if is_valid['status'] == True:
        request.session['user_id'] = is_valid['user'].id
        return redirect('/home')
    else:
        if is_valid['status'] == False:
            messages.error(request, is_valid['message'])
        return redirect('/login')
# END ALL LOGGING FUNCTIONS*********
