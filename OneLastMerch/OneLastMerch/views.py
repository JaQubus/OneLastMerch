from django.shortcuts import render

# Main view
def index(request):
    user = request.user # cheks if user is loged in, makes that variable go further in templates
    context = {"user": user}
    # print(user)
    return render(request, 'base/index.html', context)
