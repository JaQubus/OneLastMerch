from django.shortcuts import render
from .settings import STATIC_ROOT

# Main view
def index(request):
    print(f"STATIC_ROOT is set to: {STATIC_ROOT}")
    user = request.user # cheks if user is loged in, makes that variable go further in templates
    context = {"user": user}
    # print(user)
    return render(request, 'base/index.html', context)
