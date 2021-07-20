from django import forms
from django.forms import ModelForm

from core.mixins.bootstrap_form import BootstrapFormMixin
from grocery_store.grocery_auth.models import GroceryUser
from grocery_store.profiles.models import Profile


class ProfileForm(forms.ModelForm, BootstrapFormMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()

    class Meta:
        model = Profile
        exclude = ('user',)


class EditProfileForm(ModelForm):

    class Meta:
        model = GroceryUser
        fields = (
            'email',
        )
