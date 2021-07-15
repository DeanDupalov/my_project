from django import forms
from django.contrib.auth import authenticate


class SignInForm(forms.Form):
    user = None
    username = forms.CharField(
        max_length=20,
    )

    password = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(),
    )

    def clean_password(self):
        self.user = authenticate(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )

        if not self.user:
            raise forms.ValidationError('Username and /or password are incorrect!')

    def save(self):
        return self.user
