from django.urls import path

from grocery_store.store.views import index, list_products, add_product, edit_product, delete_products, product_details

urlpatterns = [
    path('', index, name='landing page'),
    path('list/', list_products, name='list products'),
    path('add/', add_product, name='add product'),
    path('details/<int:pk>', product_details, name='product details'),
    path('edit/<int:pk>', edit_product, name='edit product'),
    path('delete/<int:pk>', delete_products, name='delete product'),
]
