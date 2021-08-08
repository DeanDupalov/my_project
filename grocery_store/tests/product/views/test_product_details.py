from django.test import TestCase, Client
from django.urls import reverse

from core.image_file_testing import get_image_file
from grocery_store.product.models import Product, Category


class ProductDetailsView(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_getProductDetails_shouldRenderCorrectTemplate(self):
        product = Product.objects.create(
            name='Carrot',
            price=1,
            description='Lorem',
            image=get_image_file(),
            category=Category.objects.create(type=Category.FRUITS),
        )
        response = self.test_client.get(reverse('product details', kwargs={'pk': product.pk}))

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed('grocery/profile/product-details.html')


