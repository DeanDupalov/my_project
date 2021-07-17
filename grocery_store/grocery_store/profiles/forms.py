from django import forms

from grocery_store.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
