from django.urls import path

from grocery_store.grocery_auth.views import sign_in, sign_out, RegisterView

urlpatterns = [
    path('sign-up/', RegisterView.as_view(), name='sign up'),
    path('sign-in/', sign_in, name='sign in'),
    path('sign-out/', sign_out, name='sign out'),
]