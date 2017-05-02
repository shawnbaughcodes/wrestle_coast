from django.shortcuts import render
from login_and_registration import *
from browse import *
# Create your views here.
def index(request):
    return render(request, 'company/index.html')

def logout(request):
    request.session.clear()
    return redirect('/')
