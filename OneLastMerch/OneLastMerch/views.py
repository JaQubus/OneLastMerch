from django.shortcuts import render

def index(request):
    print(request.session.items())
    print(request.user.is_authenticated)
    return render(request, 'base/index.html')
