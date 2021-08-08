from django.urls import path

from grocery_store.profiles.views import edit_profile, profile_details, ChangePasswordView

urlpatterns = [
    path('profile_details/', profile_details, name='profile details'),
    path('edit_profile/', edit_profile, name='edit profile'),
    path('change_password', ChangePasswordView.as_view(), name='change password'),
]
