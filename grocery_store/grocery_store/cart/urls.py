from django.conf.urls import url
from django.urls import path

from grocery_store.cart.views import add_to_cart, delete_one_from_cart, OrderSummaryView, delete_from_cart

urlpatterns = [
    path('order_detail/', OrderSummaryView.as_view(), name='order details'),
    path('add_to_cart/<int:pk>', add_to_cart, name='add to cart'),
    path('delete_one_from_car/<int:pk>', delete_one_from_cart, name='delete one item from cart'),
    path('delete_from_car/<int:pk>', delete_from_cart, name='delete item from cart'),
]