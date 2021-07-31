from django import forms
from django.core.exceptions import ValidationError

from core.mixins.bootstrap_form import BootstrapFormMixin
from grocery_store.product.models import Product, DiscountProduct


class ProductCreateForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()

    class Meta:
        model = Product
        fields = '__all__'


class DiscountProductForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()

    class Meta:
        model = DiscountProduct
        fields = '__all__'

    def clean(self):
        if self.cleaned_data['price'] >= self.cleaned_data['product'].price:
            raise ValidationError('New price must be lower than current price.')
        return self.cleaned_data