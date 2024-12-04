from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'base/index.html')

def register(request):
    return render(request, 'base/register.html')
