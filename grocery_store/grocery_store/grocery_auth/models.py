from django.contrib.auth.base_user import AbstractBaseUser

from django.contrib.auth.models import PermissionsMixin, User
from django.db import models

from grocery_store.grocery_auth.manager import GroceryUserManager


class GroceryUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'

    objects = GroceryUserManager()


from .signals import *
