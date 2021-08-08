
from django.test import TestCase, Client
from django.urls import reverse

from core.image_file_testing import get_image_file
from grocery_store.product.models import Product, Category, DiscountProduct


class IndexViewTests(TestCase):

    def setUp(self):
        self.test_client = Client()

    def test_IndexView_whenProductsLessOrEqual3_shouldRenderCorrectTemplate(self):

        product = Product.objects.create(
            name='Name',
            price=1,
            description='Lorem',
            image=get_image_file(),
            category=Category.objects.create(type='Fruits'),
        )

        response = self.test_client.get(reverse('landing page'))
        self.assertTemplateUsed('grocery/index.html')

        products = response.context['products']
        products = response.context['categories']
        self.assertLessEqual(len(products), 3)

    def test_IndexView_whenNoProducts_shouldRenderCorrectTemplateWithNoProducts(self):
        response = self.test_client.get(reverse('landing page'))
        self.assertTemplateUsed('grocery/index.html')

        products = response.context['products']
        self.assertEqual(0, len(products))

    def test_IndexView_whenDiscountedProducts_shouldRenderCorrectTemplateWithDiscountedProducts(self):
        product = Product.objects.create(
            name='Name',
            price=3,
            description='Lorem',
            image=get_image_file(),
            category=Category.objects.create(type='Fruits'),
        )
        discounted_product = DiscountProduct.objects.create(
            product=product,
            price=1.5,
        )
        response = self.test_client.get(reverse('landing page'))
        self.assertTemplateUsed('grocery/index.html')

        discounted_products = response.context['discounted_products']
        self.assertIsNotNone(discounted_products)

    def test_IndexView_whenNoDiscountedProducts_shouldRenderCorrectTemplate(self):
        product = Product.objects.create(
            name='Name',
            price=3,
            description='Lorem',
            image=get_image_file(),
            category=Category.objects.create(type='Fruits'),
        )
        response = self.test_client.get(reverse('landing page'))
        self.assertTemplateUsed('grocery/index.html')

        discounted_products = response.context['discounted_products']
        self.assertEqual(0, len(discounted_products))


    def test_IndexView_whenCategories_shouldRenderCorrectTemplate(self):
        category = Category.objects.create(type='Fruits')
        product = Product.objects.create(
            name='Name',
            price=3,
            description='Lorem',
            image=get_image_file(),
            category=category,
        )
        response = self.test_client.get(reverse('landing page'))
        self.assertTemplateUsed('grocery/index.html')

        categories = response.context['categories']
        self.assertEqual(1, len(categories))

    def test_IndexView_whenNoCategories_shouldRenderCorrectTemplateWithoutCategories(self):

        response = self.test_client.get(reverse('landing page'))
        self.assertTemplateUsed('grocery/index.html')

        categories = response.context['categories']
        self.assertEqual(0, len(categories))