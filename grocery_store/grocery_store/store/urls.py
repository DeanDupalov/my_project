from django.urls import path

from grocery_store.store.views import edit_product, delete_products, \
    list_category_products, IndexView, ListAllProductsView, AddProduct, contact_view, product_details

urlpatterns = [
    path('', IndexView.as_view(), name='landing page'),
    path('list/', ListAllProductsView.as_view(), name='list products'),
    path('category_products/<int:pk>', list_category_products, name='list category products'),
    path('add/', AddProduct.as_view(), name='add product'),
    path('details/<int:pk>', product_details, name='product details'),
    path('edit/<int:pk>', edit_product, name='edit product'),
    path('delete/<int:pk>', delete_products, name='delete product'),
    path('contact/', contact_view, name='contact'),
]
