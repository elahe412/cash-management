from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models.user import CustomUser


@admin.register(CustomUser)
class UserAdmin(DjangoUserAdmin):
    list_display = ['id', 'username', 'email']
    search_fields = ['username', 'email']
    list_filter = ['is_superuser', 'is_active', 'is_staff']
    list_display_links = ['email']
