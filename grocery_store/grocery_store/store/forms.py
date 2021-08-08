from django import forms

from core.mixins.bootstrap_form import BootstrapFormMixin


class ContactForm(forms.Form, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()

    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    subject = forms.CharField(required=True)
    email = forms.EmailField(max_length=200, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
