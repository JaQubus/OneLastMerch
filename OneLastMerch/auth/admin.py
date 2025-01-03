from django.contrib import admin
from .models import User

@admin.register(User)
class OLM_User(admin.ModelAdmin):
    list_display = ('email', 'username', 'password')
    search_fields = ('email', 'username')
