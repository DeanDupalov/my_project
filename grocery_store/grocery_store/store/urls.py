from django.urls import path

from grocery_store.store.views import IndexView, ListAllProductsView, list_category_products, contact_view

urlpatterns = [
    path('', IndexView.as_view(), name='landing page'),
    path('list/', ListAllProductsView.as_view(), name='list products'),
    path('category_products/<int:pk>', list_category_products, name='list category products'),
    path('contact/', contact_view, name='contact'),
]
