from django.contrib.auth import get_user_model
from django.db import models

from grocery_store.store.models import Product

UserModel = get_user_model()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=30,
    )
    surname = models.CharField(
        max_length=30,
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.first_name

