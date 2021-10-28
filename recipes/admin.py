from django.contrib import admin

from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """
    Recipe admin model
    """

    list_display = ["id", "title", "created"]
