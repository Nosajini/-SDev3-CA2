from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models
from .forms import CustomUserCreationForm
from .models import CustomUser, Profile

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ['username', 'email', 'location', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
