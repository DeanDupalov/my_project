from django import forms

from core.mixins.bootstrap_form import BootstrapFormMixin


class CheckoutForm(forms.Form, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()

    shipping_address = forms.CharField(required=False)
    shipping_country = forms.CharField(required=False)
    shipping_zip = forms.CharField(required=False)

    billing_address = forms.CharField(required=False)
    billing_country = forms.CharField(required=False)
    billing_zip = forms.CharField(required=False)

