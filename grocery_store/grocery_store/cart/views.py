from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect, render

from django.views import View


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
class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            user_profile = get_object_or_404(Profile, user=self.request.user)
            order = Order.objects.get(user=user_profile, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'grocery/cart/order_summary.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")

@login_required()
def add_to_cart(request, pk):
    item = Product.objects.get(pk=pk)
    user_profile = get_object_or_404(Profile, user=request.user)

    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=user_profile,
        ordered=False,
    )

    order_qs = Order.objects.filter(
        user=user_profile,
        ordered=False,
    )

    if order_qs.exists():
        order = order_qs[0]
        if order_item in order.items.all():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This product quantity was updated.")
            return redirect("order details")
        else:
            order.items.add(order_item)
            messages.info(request, "This product was added to your cart.")
            return redirect("order details")
    else:
        order = Order.objects.create(user=user_profile)
        order.items.add(order_item)

        return redirect('landing page')


@login_required()
def delete_from_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    user_profile = get_object_or_404(Profile, user=request.user)

    order_qs = Order.objects.filter(
        user=user_profile,
        ordered=False,
    )
    if order_qs.exists():
        order = order_qs[0]

        order_item = OrderItem.objects.filter(
            item=item,
            user=user_profile,
            ordered=False,
        )[0]
        if order_item.quantity > 1:
            order_item.quantity -= 1
            order_item.save()
            messages.info(request, "This item quantity was reduced.")
        else:
            order.items.remove(order_item)
            messages.info(request, "This item was removed.")
        return redirect("order details")

    else:
        messages.info(request, "You do not have an active order")
        return redirect('list products')




