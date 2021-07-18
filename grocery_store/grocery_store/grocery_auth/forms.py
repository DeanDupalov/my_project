from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm

from core.mixins.bootstrap_form import BootstrapFormMixin

UserModel = get_user_model()


class SignUpForm(UserCreationForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()
    class Meta:
        model = UserModel
        fields = ('email',)


class SignInForm(forms.Form, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()

    user = None
    email = forms.EmailField()

    password = forms.CharField(
        widget=forms.PasswordInput(),
    )

    def clean_password(self):
        self.user = authenticate(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
        )

        if not self.user:
            raise forms.ValidationError('Email or password are incorrect!')

    def save(self):
        return self.user
