from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Category(models.Model):
    BAKERY = 'Bakery'
    FRUITS = 'Fruits'
    VEGETABLES = 'Vegetables'
    MEAT = 'Meat'
    RICE_AND_PASTA = 'Rice and Pasta'
    FISH_AND_SEAFOOD = 'Fish and Seafood'
    OILS_VINEGAR_AND_DRIED_HERBS = 'Oils, Vinegar and Dried herbs'
    BEER_WINE_AND_SPIRITS = 'Bear, Wine and Spirits'
    SOFT_DRINKS = 'Soft drinks'
    CRISPS_SNACKS_AND_NUTS = 'Crisps, Snacks and Nuts'
    CHOCOLATE_AND_SWEETS = 'Chocolate and Sweets'
    UNKNOWN = 'unknown'

    CATEGORY_TYPES = (
        (BAKERY, 'Bakery'),
        (FRUITS, 'Fruits'),
        (VEGETABLES, 'Vegetables'),
        (MEAT, 'Meat'),
        (RICE_AND_PASTA, 'Rice And Pasta'),
        (FISH_AND_SEAFOOD, 'Fish and Seafood'),
        (OILS_VINEGAR_AND_DRIED_HERBS, 'Oils, Vinegar and Dried Herbs'),
        (BEER_WINE_AND_SPIRITS, 'Bear, Wine and Spirits'),
        (SOFT_DRINKS, 'Soft Drinks'),
        (CRISPS_SNACKS_AND_NUTS, 'Crisps, Snacks and Nuts'),
        (CHOCOLATE_AND_SWEETS, 'Chocolate and Sweets'),
        (UNKNOWN, 'Unknown'),
    )
    type = models.CharField(max_length=60, choices=CATEGORY_TYPES, default='UNKNOWN', blank=False)

    def __str__(self):
        return self.type


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="price",
        validators=[MinValueValidator(0.0)],
    )
    description = models.TextField()
    image = models.ImageField(upload_to='product')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True, verbose_name='created')
    updated = models.DateTimeField(auto_now=True, verbose_name='updated')

    def __str__(self):
        return self.name


class DiscountProduct(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.0)],
    )

    def __str__(self):
        return self.product.name


class Like(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # test = models.CharField(max_length=3, default='foo')
    # user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
