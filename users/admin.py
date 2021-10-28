from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    User admin model
    """

    list_display = ["id", "username", "email", "is_active", "is_staff", "is_superuser"]
