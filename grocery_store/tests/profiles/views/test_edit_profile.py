from django.test import TestCase, Client
from django.urls import reverse

from grocery_store.grocery_auth.models import GroceryUser
from grocery_store.profiles.models import Profile


class EditProfileView(TestCase):
    def setUp(self):
        self.test_client = Client()
        self.user = GroceryUser.objects.create_user(
            email='test@abv.bg',
            password='qwe123'
        )

        self.test_client.login(email='test@abv.bg', password='qwe123')

    def test_getEditProfile_shouldRenderRightTemplate(self):
        response = self.test_client.get(reverse('edit profile'))
        self.assertTemplateUsed('grocery/profile/edit-profile.html')

        user_form = response.context['user_form']
        self.assertIsNotNone(user_form)

        profile_form = response.context['profile_form']
        self.assertIsNotNone(profile_form)

        address_form = response.context['profile_address_form']
        self.assertIsNotNone(address_form)

    # def test_postEditProfile_whenValidData_shouldRedirectToProfileDetails(self):
    #     data = {
    #         'first_name': 'First',
    #         'surname': 'Surname',
    #         'street_address': 'test street',
    #         'apartment_number': 11,
    #         'town': 'Sofia',
    #         'country': 'Bulgaria',
    #         'zip': '5000'
    #     }
    #     response = self.test_client.post(reverse('edit profile'), data=data)
    #     self.assertRedirects(response, reverse('profile details'))

    def test_postEditProfile_whenInvalidData_shouldRenderEditProfileAndContainsErrors(self):
        pass