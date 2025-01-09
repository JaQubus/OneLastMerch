# Import necessary modules
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import RegisterForm, LoginForm
from .models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Handle user registration
def register(request):
    if request.method == 'POST':  # Check if the form is submitted
        form = RegisterForm(request.POST)  # Populate the form with POST data
        if form.is_valid():  # Validate form data
            # Extract cleaned data from the form
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            is_correct = True

            # Check if the email already exists in the database
            if User.objects.filter(email=email).exists():
                form.add_error('email', 'This email is already used.')  # Add an error message
                is_correct = False

            # Check if the username already exists in the database
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'This username is already used.')  # Add an error message
                is_correct = False

            if is_correct:  # Proceed if no errors
                # Create a new user with the given details
                user = User.objects.create_user(username=username, email=email, password=password)

                # Authenticate the newly created user
                user_authenticated = authenticate(request, email=email, password=password)

                if user_authenticated is not None:
                    # Log the user in and redirect to the home page
                    login(request, user_authenticated)
                    return redirect('/')
                else:
                    # Authentication failed for some reason
                    print("Authentication failed for the newly created user.")
    else:
        # If the request is not POST, render an empty registration form
        form = RegisterForm()

    # Render the registration page with the form
    return render(request, 'auth_templates/register.html', {'form': form})

# Display all users as a JSON response
# is disabled for obvious reasons, only used in testing
def show_users(request):
    # Query all users and include username, email, and password fields
    users = User.objects.all().values('username', 'email', 'password')
    return JsonResponse(list(users), safe=False)

# Handle user login
# The defauly view when unlogged user tries to get to a '@login_required' page
def login_auth(request):
    # Just to add a fancy feature, example: user goes to /account because he had it saved in browser or any other reason.
    # Now the user needs to log in again, because of various reasons. To give Them a good experience with the page, after log in it takes them back to /account 
    if request.GET.get("next"):  # Store the 'next' parameter in the session if present
        request.session['next'] = request.GET.get("next")

    if request.method == 'POST':  # Check if the form is submitted
        form = LoginForm(request.POST)  # Populate the form with POST data
        if form.is_valid():  # Validate form data
            # Extract cleaned data
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Authenticate the user
            user = authenticate(request, email=email, password=password)

            if not user:  # If authentication fails, add an error message
                form.add_error('password', 'Email or password incorrect')
            else:
                # Log the user in
                login(request, user)
                # Redirect to the 'next' page if it was stored in the session
                if 'next' in request.session:
                    next = request.session['next']
                    del request.session['next']  # Remove 'next' from session
                    return redirect("" + next)
                
                # Otherwise, redirect to the home page
                return redirect("/")
    else:
        # If the request is not POST, render an empty login form
        form = LoginForm()

    # Render the login page with the form
    return render(request, 'auth_templates/login.html', {'form': form})

# Handle user logout
# I think that giving this endpoint a '@login_required' is not necessary. May be wrong though
def logout_auth(request):
    logout(request)  # Log the user out
    return redirect('/')  # Redirect to the home page

# Handle password change for logged-in users
@login_required  # Ensure the user is logged in to access this view
def change_password(request):
    user = request.user  # Get the currently logged-in user
    if request.method == "POST":  # Check if the form is submitted
        form = PasswordChangeForm(user, request.POST)  # Populate the form with POST data
        if form.is_valid():  # Validate form data
            # Extract old and new passwords
            old_password = form.cleaned_data["old_password"]
            new_password = form.cleaned_data["new_password1"]

            # Authenticate the user with the old password
            user = authenticate(request=request, email=request.user, password=old_password)
            if not user:  # If authentication fails, add an error message
                form.add_error('password', 'Password incorrect')
            else:
                # Update the user's password and save the changes
                user.set_password(new_password)
                user.save()

                # Log the user in again after changing the password
                login(request, user)

            # Render the page with a success message
            return render(request, 'ui/change_password.html', {"success": "User password changed successfully"})
    else:
        # If the request is not POST, render an empty password change form
        form = PasswordChangeForm(user=user)

    # Render the password change page with the form
    return render(request, 'ui/change_password.html', {"form": form})
