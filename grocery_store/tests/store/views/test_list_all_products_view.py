from django.test import TestCase, Client
from django.urls import reverse

from core.image_file_testing import get_image_file
from grocery_store.product.models import Product, Category


class ListAllProductsViewTest(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_ListAllProductsView_whenProducts_shouldRenderCorrectTemplateWhitProducts(self):
        product = Product.objects.create(
            name='Carrot',
            price=1,
            description='Lorem',
            image=get_image_file(),
            category=Category.objects.create(type='Vegetables'),
        )
        response = self.test_client.get(reverse('list products'))
        self.assertTemplateUsed('grocery/items-list.html')

        products = response.context['products']
        self.assertLessEqual(len(products), 1)

    def test_ListAllProductsView_whenNoProducts_shouldRenderCorrectTemplateWhitNoProducts(self):
        response = self.test_client.get(reverse('list products'))
        self.assertTemplateUsed('grocery/items-list.html')

        products = response.context['products']
        self.assertEqual(0, len(products))


    def test_ListAllProductsView_whenCategories_shouldRenderCorrectTemplate(self):
        category = Category.objects.create(type='Fruits')
        product = Product.objects.create(
            name='Name',
            price=3,
            description='Lorem',
            image=get_image_file(),
            category=category,
        )
        response = self.test_client.get(reverse('list products'))
        self.assertTemplateUsed('grocery/items-list.html')

        categories = response.context['categories']
        self.assertEqual(1, len(categories))

    def test_ListAllProductsView_whenNoCategories_shouldRenderCorrectTemplateWithoutCategories(self):

        response = self.test_client.get(reverse('list products'))
        self.assertTemplateUsed('grocery/items-list.html')

        categories = response.context['categories']
        self.assertEqual(0, len(categories))
