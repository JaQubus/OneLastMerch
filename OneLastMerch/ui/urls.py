from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.shop, name='shop'),
    path('shop/<str:filter>/', views.shop_filter, name='shop'),
    path('about-us/', views.about_us, name='shop'),
    path('contact/', views.contact, name='shop'),
    path('account', views.account, name="account"),
    # path('load_items', views.load_items, name="load_items")
]
