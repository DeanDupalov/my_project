from django.urls import path

from grocery_store.store.views import index, list_products

urlpatterns = [
    path('', index, name='landing page'),
    path('list/', list_products, name='list products'),
]