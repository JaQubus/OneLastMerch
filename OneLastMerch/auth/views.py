from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import RegisterForm, LoginForm
from django.contrib.auth.hashers import make_password, check_password
from .models import User

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            if User.objects.filter(email=email).exists():
                form.add_error('email', 'This email is already used.')

            else:
                hashed_password = make_password(password)

                User.objects.create(username=username, email=email, password=hashed_password)

                return redirect('/')

    else:
        form = RegisterForm()

    return render(request, 'auth_templates/register.html', {'form': form})

def show_users(request):
    users = User.objects.all().values('username', 'email', 'password')
    return JsonResponse(list(users), safe=False)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.filter(email=email).first()
            
            if not User.objects.filter(email=email) or not check_password(password, user.password):
                form.add_error('password', 'Email or password incorrect')
            else:
                return redirect("/")

    else:
        form = LoginForm()

    return render(request, 'auth_templates/login.html', {'form': form})