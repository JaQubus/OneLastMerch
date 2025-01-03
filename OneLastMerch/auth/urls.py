from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('users/', views.show_users, name='show_users'),
    path('login/', views.login_auth, name='login'),
    path('logout/', views.logout_auth, name='logout')
]
