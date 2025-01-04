from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.shop, name='shop'),
    path('shop/<str:filter>/', views.shop_filter, name='shop-filter'),
    path('about-us/', views.about_us, name='about-us'),
    path('contact/', views.contact, name='contact'),
    path('account/', views.account, name="account"),
    # path('load_items', views.load_items, name="load_items")
]
