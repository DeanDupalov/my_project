from django.urls import path

from grocery_store.product.views import AddProduct, product_details, edit_product, delete_products, AddDiscountProduct
urlpatterns = [
    path('add/', AddProduct.as_view(), name='add product'),
    path('details/<int:pk>', product_details, name='product details'),
    path('edit/<int:pk>', edit_product, name='edit product'),
    path('delete/<int:pk>', delete_products, name='delete product'),
    path('add_discount/', AddDiscountProduct.as_view(), name='add discounted product'),
]
