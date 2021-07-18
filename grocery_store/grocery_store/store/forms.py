from django import forms

from core.mixins.bootstrap_form import BootstrapFormMixin
from grocery_store.store.models import Product


class ProductCreateForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()

    class Meta:
        model = Product
        fields = '__all__'
