from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import RegisterForm, LoginForm
from django.contrib.auth.hashers import check_password
from .models import User
from django.contrib.auth import login, authenticate, logout

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            is_correct = True

            # Check if the email or username already exists
            if User.objects.filter(email=email).exists():
                form.add_error('email', 'This email is already used.')
                is_correct = False
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'This username is already used.')
                is_correct = False

            if is_correct:
                # Create the user
                user = User.objects.create_user(username=username, email=email, password=password)

                # print(f"Password before hashing: {password}")
                # print(f"Password in the database (hashed): {user.password}")
                # print(f"Attempting to authenticate with email: {email} and password: {password}")

                # Authenticate using the custom backend
                user_authenticated = authenticate(request, email=email, password=password)

                if user_authenticated is not None:
                    # print("Authentication successful.")
                    login(request, user_authenticated)
                    return redirect('/')
                else:
                    print("Authentication failed for the newly created user.")
                    # print(f"User exists: {User.objects.filter(email=email).exists()}")
                    # print(f"Password check (should be True): {user.check_password(password)}")
    else:
        form = RegisterForm()

    return render(request, 'auth_templates/register.html', {'form': form})


def show_users(request):
    users = User.objects.all().values('username', 'email', 'password')
    return JsonResponse(list(users), safe=False)

def login_auth(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)
            
            if not user:
                form.add_error('password', 'Email or password incorrect')
            else:
                login(request, user)
                return redirect("/")

    else:
        form = LoginForm()

    return render(request, 'auth_templates/login.html', {'form': form})

def logout_auth(request):
    logout(request)
    return redirect('/')