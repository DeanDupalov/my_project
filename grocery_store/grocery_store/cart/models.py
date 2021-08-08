from django.db import models
from grocery_store.product.models import Product
from grocery_store.profiles.models import Profile


class OrderItem(models.Model):
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.item.name

    def get_total_item_price(self):
        return self.quantity * self.item.price


class Order(models.Model):
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        result = 0
        for order_item in self.items.all():
            result += order_item.get_total_item_price()
        return result

    def __str__(self):
        return f"{self.user} - {self.user_id}"
