from django import forms
from core.mixins.bootstrap_form import BootstrapFormMixin
from grocery_store.profiles.models import Profile, ProfileAddress


class ProfileForm(forms.ModelForm, BootstrapFormMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()

    class Meta:
        model = Profile
        exclude = ('user', 'products')


class ProfileAddressForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()

    class Meta:
        model = ProfileAddress
        exclude = ('profile',)


class DisabledProfileAddressForm(ProfileAddressForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
