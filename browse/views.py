from django.shortcuts import render
import os
# Create your views here.
def index(request):
    print '*'*50
    # os.environ['test'] = 'data'
    print os.environ.get('test')
    print '*'*50
    return render(request, 'browse/index.html')
