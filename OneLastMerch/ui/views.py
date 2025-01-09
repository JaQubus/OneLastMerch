# Import necessary modules
from django.shortcuts import render, redirect
import os
from .models import Item
from .forms import ContactForm, FilterForm
from dotenv import load_dotenv
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from auth.models import User

# Load environment variables from .env file
load_dotenv()

# Display the shop page with items and *optional* filtering by tags
# Uses filtering based on a form
def shop(request):
    if request.method == "POST" and request.POST.getlist("tags"):  # Check if a POST request with tags is made
        tags = request.POST.getlist("tags")  # Get selected tags from the POST data
        print(tags)  # Debug: print selected tags
        form = FilterForm(request.POST)  # Populate the filter form with POST data
        # Filter items by tags and pass to the context
        context = {
            "items": Item.objects.all().values("title", "price", "image").filter(tag__in=tags),
            "form": form
        }
    else:
        # If no filter is applied, display all items
        form = FilterForm()
        context = {
            "items": Item.objects.all().values("title", "price", "image"),
            "form": form
        }
    return render(request, 'ui/shop.html', context=context)  # Render the shop page with items and form

# Display the shop page with items filtered by a specific tag
# IMPORTANT THE PAGE IF NO TAG IS FOUND, RESERTS TO MAIN VIEW. 
# MAKES USERS NOT GUESS THE ITEMS THAT MAY BE HIDDEN BUT IN DATABASE
def shop_filter(request, filter):
    form = FilterForm()  # Create an empty filter form
    # Filter items by a specific tag
    items = {
        "items": Item.objects.all().values("title", "price", "image").filter(tag=filter),
        "form": form
    }

    # Render the shop page with the filtered items
    if items:
        return render(request, 'ui/shop.html', items)
    return render(request, 'ui/shop.html')  # Render an empty shop page if no items match

# Render the About Us page
def about_us(request):
    return render(request, 'ui/about-us.html')

# Handle the Contact Us form
def contact(request):
    print(request.method)  # Debug: print the HTTP method of the request
    if request.method == 'POST':  # Check if the form is submitted
        form = ContactForm(request.POST)  # Populate the form with POST data
        if form.is_valid():  # Validate the form data
            # Extract cleaned data
            sender_email = form.cleaned_data["sender"]
            content = form.cleaned_data["content"]

            # Define the receiver email (read from environment variable)
            receiver_list = [os.getenv("RECEIVER_EMAIL")]  # Must be a list

            # Construct email subject and message
            subject = f"Feedback from {sender_email} OneLastMerch"
            message = f"OneLastMerch \nEmail: {sender_email}\n\nFeedback:\n{content}"
            from_email = sender_email  # Use sender's email as 'from' address

            # Send the email
            send_mail(subject, message, from_email, receiver_list)
            print("Sending confirmed")  # Debug: print confirmation of sending
            return render(request, 'ui/contact.html', {"success": "Thank you for your feedback"})  # Display success message
    else:
        # If the request is not POST, render an empty contact form
        form = ContactForm()
    return render(request, 'ui/contact.html', {"form": form})  # Render the contact page with the form

# Display the account page for the logged-in user
@login_required  # Ensure the user is logged in to access this view
def account(request):
    '''
    User.objects.all().filter(email=request.user).values("username").first()["username"]
    Explanation:
    - User.objects.all() gets all user data.
    - The filter() method acts as an SQL 'WHERE' clause.
    - The values() method fetches specific column values (returns a QuerySet).
    - The first() method converts the QuerySet into a dictionary.
    '''
    # Fetch the username and email for the logged-in user
    context = {
        "username": User.objects.all().filter(email=request.user).values("username").first()["username"],
        "email": request.user
    }
    return render(request, 'ui/account.html', context=context)  # Render the account page with user data

# Load item images from a directory and save them to the database
# only used to add (sadly) fictional items to the store/database
def load_items(request):
    print(os.getcwd())  # Debug: print the current working directory
    # Iterate through all files in the specified directory
    for image in os.listdir("OneLastMerch/static/items_images"):
        # Check if the file is an image (by extension)
        if image.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Create a new item with the image name
            item = Item(image=image)
            item.save()  # Save the item to the database
    return redirect("/")  # Redirect to the home page after loading items
