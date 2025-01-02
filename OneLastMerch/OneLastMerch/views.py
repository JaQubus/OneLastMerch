from django.shortcuts import render

def index(request):
    print(request.session.items())
    return render(request, 'base/index.html')
