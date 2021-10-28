from uuid import uuid4

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User Model
    - we use uuidv4 as the id field
    - password field can be null since API users are handled via Auth0
      (we still need password field for the superuser, though)
    """

    id = models.UUIDField(db_index=True, default=uuid4, editable=False, primary_key=True)
    email = models.EmailField("email address", unique=True)
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

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name
