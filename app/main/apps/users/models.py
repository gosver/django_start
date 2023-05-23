from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

from django.db import models
from django.utils.translation import gettext_lazy as _


# Users table
class User(AbstractUser):
    username = None
    email = models.EmailField(_("Ваш E-mail"), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
