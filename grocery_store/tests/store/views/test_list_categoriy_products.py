from django.test import TestCase, Client
from django.urls import reverse

from core.image_file_testing import get_image_file
from grocery_store.product.models import Product, Category


class ListCategoryProductsViewTest(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_ListCategoryProductsView_shouldRenderCorrectTemplateWhitProductsFromATheSameCategory(self):
        category = Category.objects.create(type='Fruits')
        product = Product.objects.create(
            name='Carrot',
            price=1,
            description='Lorem',
            image=get_image_file(),
            category=Category.objects.create(type='Vegetables'),
        )
        product_two = Product.objects.create(
            name='Apple',
            price=2,
            description='Lorem',
            image=get_image_file(),
            category=category,
        )
        response = self.test_client.get(reverse('list category products', kwargs={'pk': category.pk}))
        self.assertTemplateUsed('grocery/items-list.html')

        products = response.context['products']
        self.assertLessEqual(len(products), 1)
        self.assertEqual(products[0].category.type, 'Fruits')



    def test_ListCategoryProductsView_whenCategories_shouldRenderCorrectTemplate(self):
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

    def test_ListCategoryProductsView_whenNoCategories_shouldRenderCorrectTemplateWithoutCategories(self):
        response = self.test_client.get(reverse('landing page'))
        self.assertTemplateUsed('grocery/index.html')

        categories = response.context['categories']
        self.assertEqual(0, len(categories))
