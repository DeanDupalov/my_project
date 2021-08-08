from django.test import TestCase, Client
from django.urls import reverse

from core.image_file_testing import get_image_file
from grocery_store.grocery_auth.models import GroceryUser
from grocery_store.product.models import Product, Category



class EditProductViewTest(TestCase):
    def setUp(self):
        self.test_client = Client()
        self.user = GroceryUser.objects.create_user(
            email='test@abv.bg',
            password='qwe123'
        )

        self.test_client.login(email='test@abv.bg', password='qwe123')

    def test_getEditProductView_shouldRenderCorrectTemplate(self):
        product = Product.objects.create(
            name='Name',
            price=1,
            description='Lorem',
            image=get_image_file(),
            category=Category.objects.create(type=Category.FRUITS),
        )

        response = self.test_client.get(reverse('edit product', kwargs={'pk': product.id}))
        self.assertTemplateUsed('grocery/product/edit-product.html')
        form = response.context['form']
        self.assertIsNotNone(form)
        self.assertEqual(200, response.status_code)

    def test_postEditProductView_whenWrongPriceShouldRenderEditProductAndContainErrors(self):
        product = Product.objects.create(
            name='Name',
            price=1,
            description='Lorem',
            image=get_image_file(),
            category=Category.objects.create(type=Category.FRUITS),
        )

        data = {
            'name': 'Name',
            'price': 'wrong Price',
            'description': 'Lorem',
            'image': get_image_file(),
            "category": Category.objects.create(type=Category.FRUITS),
        }
        response = self.test_client.post(reverse('edit product', kwargs={'pk': product.id}), data=data)
        self.assertTemplateUsed('grocery/product/edit-product.html')

        form = response.context['form']
        self.assertIsNotNone(form.errors['price'])

    def test_postEditProductView_whenValidForm_ShouldRedirectProductDetails(self):
        product = Product.objects.create(
            name='Name',
            price=1,
            description='Lorem',
            image=get_image_file(),
            category=Category.objects.create(type=Category.FRUITS),
        )
        data = {
            'name': 'Name',
            'price': 3.5,
            'description': 'Lorem',
            'image': get_image_file(),
            "category": 'Fruits',
        }
        response = self.test_client.post(reverse('edit product', kwargs={'pk': product.id}), data=data)

        self.assertRedirects(response, reverse('product details', kwargs={'pk': product.id}))