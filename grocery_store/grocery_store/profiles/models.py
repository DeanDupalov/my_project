from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

from grocery_store.product.models import Product

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


ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)


class ProfileAddress(models.Model):
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    street_address = models.CharField(max_length=100, blank=True)
    apartment_number = models.IntegerField(null=True, validators=[MinValueValidator(1)])
    town = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    zip = models.CharField(max_length=100, blank=True)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES, blank=True)

    def __str__(self):
        return f"{self.profile.first_name} {self.profile.first_name}"

    class Meta:
        verbose_name_plural = 'Addresses'
