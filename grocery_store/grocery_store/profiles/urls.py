from django.urls import path

from grocery_store.profiles.views import edit_profile

urlpatterns = [
    path('edit_profile/', edit_profile, name="edit profile")
]
