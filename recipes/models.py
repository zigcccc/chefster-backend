from django.db import models
from django.conf import settings

from helpers.models import BaseModel


class Recipe(BaseModel):
    """
    Recipe Model
    """

    title = models.CharField(max_length=80, unique=True)
    description = models.TextField(max_length=None)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ["created"]
        verbose_name = "Recipe"

    def __str__(self):
        return self.title
