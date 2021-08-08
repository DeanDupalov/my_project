from grocery_store.cart.models import Order
from grocery_store.grocery_auth.models import GroceryUser
from grocery_store.product.models import Product
from grocery_store.profiles.models import Profile


class GroceryTestUtils:


    def create_profile(self, **kwargs):
        return Profile.objects.create()

    def create_product(self, **kwargs):
        return Product.objects.create(**kwargs)

    def create_order_item(self, **kwargs):
        pass

    def create_order(self, **kwargs):
        return Order.objects.create()
