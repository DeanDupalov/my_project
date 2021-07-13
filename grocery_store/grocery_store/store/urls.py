from django.urls import path

from grocery_store.store.views import index, list_products, add_product, edit_product, delete_products, details_product

urlpatterns = [
    path('', index, name='landing page'),
    path('list/', list_products, name='list products'),
    path('details/', details_product, name='details product'),
    path('add/', add_product, name='add product'),
    path('edit/<int:pk>', edit_product, name='edit product'),
    path('delete/<int:pk>', delete_products, name='delete product'),
]