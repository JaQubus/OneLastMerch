from django.shortcuts import render

# Create your views here.

def index(request):
    print(request)
    return render(request, 'login/index.html')
