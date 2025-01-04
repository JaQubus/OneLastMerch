from django.shortcuts import render, redirect
import os
from .models import Item
from .forms import ContactForm
from dotenv import load_dotenv
from django.core.mail import send_mail

load_dotenv()



def shop(request):
    items = {"items": Item.objects.all().values("title", "price", "image")}
    return render(request, 'ui/shop.html', items)

def shop_filter(request, filter):
    items = {"items": Item.objects.all().values("title", "price", "image").filter(tag=filter)}
    return render(request, 'ui/shop.html', items)

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

def account(request):
    return render(request, 'ui/account.html')

def load_items(request):
    print(os.getcwd())
    for image in os.listdir("OneLastMerch/static/items_images"):
        if image.lower().endswith(('.png','.jpg', '.jpeg')):
            item = Item(image=image)
            item.save()
    return redirect("/")