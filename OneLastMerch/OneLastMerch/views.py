from django.shortcuts import render

def index(request):
    user = request.user
    context = {"user": user}
    print(user)
    return render(request, 'base/index.html', context)
