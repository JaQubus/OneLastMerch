from django.shortcuts import render, redirect
import os
from .models import Item
from .forms import ContactForm, FilterForm
from dotenv import load_dotenv
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from auth.models import User

load_dotenv()



def shop(request):
    if request.method == "POST" and request.POST.getlist("tags"):
        tags = request.POST.getlist("tags")
        print(tags)
        form = FilterForm(request.POST)
        context = {"items": Item.objects.all().values("title", "price", "image").filter(tag__in=tags), "form": form}
    else:
        form = FilterForm()
        context = {"items": Item.objects.all().values("title", "price", "image"), "form": form}
    return render(request, 'ui/shop.html', context=context)

def shop_filter(request, filter):
    form = FilterForm()
    items = {"items": Item.objects.all().values("title", "price", "image").filter(tag=filter), "form": form}

    if items:
        return render(request, 'ui/shop.html', items)
    return render(request, 'ui/shop.html')

def about_us(request):
    return render(request, 'ui/about-us.html')

def contact(request):
    print(request.method)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_email = form.cleaned_data["sender"]
            content = form.cleaned_data["content"]

            receiver_list = [os.getenv("RECEIVER_EMAIL")] # needs to be a list

            subject = f"Feedback from {sender_email} OneLastMerch"

            message = f"OneLastMerch \nEmail: {sender_email}\n\nFeedback:\n{content}"

            from_email = sender_email

            send_mail(subject, message, from_email, receiver_list)
            print("Sending confirmed")
            return render(request, 'ui/contact.html', {"success": "Thank you for your feedback"})

    else:
        form = ContactForm()
    return render(request, 'ui/contact.html', {"form": form})

@login_required
def account(request):
    '''
    User.objects.all().filter(email=request.user).values("username").first()["username"]
    the User.objects.all() gets all user data, the filter works as SQL 'WHERE' clause,
    the values() method takes the column values that are available, but returns a QuerySet,
    the first() method turns the QuerySet into a dict
    '''
    context = {"username": User.objects.all().filter(email=request.user).values("username").first()["username"], "email": request.user}
    return render(request, 'ui/account.html', context=context)

def load_items(request):
    print(os.getcwd())
    for image in os.listdir("OneLastMerch/static/items_images"):
        if image.lower().endswith(('.png','.jpg', '.jpeg')):
            item = Item(image=image)
            item.save()
    return redirect("/")
