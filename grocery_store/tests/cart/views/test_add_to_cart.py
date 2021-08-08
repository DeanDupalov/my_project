from django.test import TestCase, Client
from django.urls import reverse

from core.image_file_testing import get_image_file
from grocery_store.cart.models import Order, OrderItem
from grocery_store.grocery_auth.models import GroceryUser
from grocery_store.product.models import Category
from grocery_store.profiles.models import Profile
from tests.grocery_test_utils import GroceryTestUtils

class AddToCartTest(TestCase, GroceryTestUtils):

    def setUp(self):
        self.client = Client()
        self.user = GroceryUser.objects.create_user(
            email='test@abv.bg',
            password='qwe123'
        )
        self.client.login(email='test@abv.bg', password='qwe123')

        self.profile = Profile.objects.get(pk=self.user.pk)
        self.product = self.create_product(
            name='Name Test',
            price=1,
            description='Lorem',
            image=get_image_file(),
            category=Category.objects.create(type=Category.FRUITS),
        )

    def test_get_whenNoItemInCart_ShouldRedirect(self):
        item = self.create_order_item(
            user=self.profile,
            order=False,
            item=self.product,
        )
        order = Order.objects.create(
            user=self.profile,
        )
        response = self.client.get(reverse('add to cart', kwargs={'pk': order.pk}))

        self.assertRedirects(response, reverse('order details'))
