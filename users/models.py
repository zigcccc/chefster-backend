from uuid import uuid4

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from constants.resources import JsonApiResource

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User Model
    - we use uuidv4 as the id field
    - password field can be null since API users are handled via Auth0
      (we still need password field for the superuser, though)
    """

    id = models.UUIDField(db_index=True, default=uuid4, editable=False, primary_key=True)
    email = models.EmailField("email address", null=True)
    username = models.CharField("username", max_length=80, unique=True)
    password = models.CharField("password", max_length=128, null=True)
    first_name = models.CharField("first name", max_length=80, blank=True)
    last_name = models.CharField("last name", max_length=80, blank=True)
    date_joined = models.DateTimeField("date joined", auto_now_add=True)
    is_active = models.BooleanField("active", default=True)
    is_staff = models.BooleanField("is staff", default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    @property
    def recipes_count(self):
        return self.recipe_set.count

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    class JSONAPIMeta:
        resource_name = JsonApiResource.USER
