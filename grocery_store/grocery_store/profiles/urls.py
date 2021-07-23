from django.urls import path

from grocery_store.profiles.views import edit_profile, profile_details

urlpatterns = [
    path('profile_details/', profile_details, name="profile details"),
    path('edit_profile/', edit_profile, name="edit profile"),
]
