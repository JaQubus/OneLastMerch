from django.shortcuts import render, redirect
import os
from .models import Item

def shop(request):
    items = {"items": Item.objects.all().values("title", "price", "image")}
    return render(request, 'ui/shop.html', items)

def shop_filter(request, filter):
    items = {"items": Item.objects.all().values("title", "price", "image").filter(tag=filter)}
    return render(request, 'ui/shop.html', items)


def about_us(request):
    return render(request, 'ui/about-us.html')

def contact(request):
    return render(request, 'ui/contact.html')

def account(request):
    return render(request, 'ui/account.html')

def load_items(request):
    print(os.getcwd())
    for image in os.listdir("OneLastMerch/static/items_images"):
        if image.lower().endswith(('.png','.jpg', '.jpeg')):
            item = Item(image=image)
            item.save()
    return redirect("/")