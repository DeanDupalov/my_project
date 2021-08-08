from django.test import TestCase, Client
from django.urls import reverse

from grocery_store.grocery_auth.models import GroceryUser


class ProfileDetailsView(TestCase):
    def setUp(self):
        self.test_client = Client()
        self.user = GroceryUser.objects.create_user(
            email='test@abv.bg',
            password='qwe123'
        )
        self.test_client.login(email='test@abv.bg', password='qwe123')

    def test_getProfileDetails_shouldRenderProfileDetails(self):
        response = self.test_client.get(reverse('profile details'))

        self.assertTemplateUsed('grocery/profile/profile_details.html')

        form = response.context['address_form']
        self.assertIsNotNone(form)