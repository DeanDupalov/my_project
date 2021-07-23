from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect

from grocery_store.cart.models import Order
from grocery_store.grocery_auth.forms import SignUpForm
from grocery_store.grocery_auth.models import GroceryUser
from grocery_store.profiles.forms import ProfileForm
from grocery_store.profiles.models import Profile


@login_required
@transaction.atomic
def edit_profile(request):
    if request.method == 'GET':
        context = {
            'user_form': SignUpForm(instance=request.user),
            'profile_form': ProfileForm(instance=Profile.objects.get(pk=request.user.pk)),
        }
        return render(request, 'grocery/profile/edit-profile.html', context)

    else:

        user_form = SignUpForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=Profile.objects.get(pk=request.user.id))

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile details')

        context = {
            'user_form': SignUpForm(instance=request.user),
            'profile_form': ProfileForm(instance=Profile.objects.get(pk=request.user.pk)),
        }
        return render(request, 'grocery/product/edit-product.html', context)


@login_required
def profile_details(request):
    profile = Profile.objects.get(pk=request.user.pk)
    profile_orders = Order.objects.filter(
        owner=profile,
    )
    context = {
        'grocery_user': request.user,
        'profile': profile,
        'profile_orders': profile_orders,
    }

    return render(request, 'grocery/profile/profile_details.html', context)
