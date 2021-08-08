from django.test import TestCase, Client
from django.urls import reverse

from grocery_store.grocery_auth.models import GroceryUser


class ContactViewTests(TestCase):

    def setUp(self):
        self.test_client = Client()
        self.user = GroceryUser.objects.create_user(
            email='test@abv.bg',
            password='qwe123'
        )
        self.test_client.login(email='test@abv.bg', password='qwe123')

    def test_getContactView_shouldReturnFormAndCorrectTemplate(self):
        response = self.test_client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('grocery/contact.html')

        form = response.context['form']
        self.assertIsNotNone(form)

    def test_postContactView_whenValidForm_shouldRedirectToLandingPage(self):
        first_name = 'Gosho'
        last_name = 'Testov'
        subject = 'test subject'
        email = 'test@abv.bg'
        message = 'test message'

        data = {
            'first_name': first_name,
            'last_name': last_name,
            'subject': subject,
            'email': email,
            'message': message,
        }

        response = self.test_client.post(reverse('contact'), data=data)

        self.assertRedirects(response, reverse('landing page'))

    def test_postContactView_whenInvalidEmail_shouldReturnContactAndErrors(self):
        first_name = 'Gosho1'
        last_name = 'Testov'
        subject = 'test subject'
        email = 'test.abv.bg'
        message = 'test message'

        data = {
            'first_name': first_name,
            'last_name': last_name,
            'subject': subject,
            'email': email,
            'message': message,
        }

        response = self.test_client.post(reverse('contact'), data=data)
        self.assertTemplateUsed(response, 'grocery/contact.html')

        form = response.context['form']
        self.assertIsNotNone(form.errors['email'])
