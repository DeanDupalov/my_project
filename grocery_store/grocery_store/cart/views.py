from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from grocery_store.cart.extrax import generate_order_id
from grocery_store.cart.models import Order, OrderItem
from grocery_store.profiles.models import Profile
from grocery_store.store.models import Product


#
# def get_user_pending_order(request):
#     user_profile = get_object_or_404(Profile, user=request.user)
#
#     order = Order.objects.filter(owner=user_profile)
#     if order.exists():
#         return order[0]
#
#     return 0


@login_required()
def add_to_cart(request, pk):
    # get the user profile
    user_profile = get_object_or_404(Profile, user=request.user)
    # filter products by id
    product = Product.objects.get(pk=pk)
    # create orderItem of the selected product
    user_order = Order.objects.get_or_create(owner=user_profile)

    order_item = OrderItem.objects.create(product=product)
    # create order associated with the user

    user_order.items.add(order_item)

    user_order.ref_code = generate_order_id()
    user_order.save()

    # show confirmation message and redirect back to the same page
    messages.info(request, "item added to cart")
    return redirect('list products')


@login_required()
def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    return redirect(reverse('shopping_cart:order_summary'))


@login_required()
def order_details(request, **kwargs):
    user_profile = get_object_or_404(Profile, user=request.user)

    existing_order = Order.objects.filter(owner=user_profile)
    context = {
        'order': existing_order
    }
    return render(request, 'grocery/cart/order_summary.html', context)
