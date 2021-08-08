from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from django.db import transaction
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from grocery_store.grocery_auth.forms import SignInForm, SignUpForm
from grocery_store.product.models import Category
from grocery_store.profiles.forms import ProfileForm, ProfileAddressForm



class RegisterView(TemplateView):
    template_name = 'grocery/auth/sign_up.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = SignUpForm()
        context['profile_form'] = ProfileForm()
        context['categories'] = Category.objects.all()

        return context

    @transaction.atomic
    def post(self, request):
        form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            address = ProfileAddressForm().save(commit=False)
            address.profile = profile
            address.save()
            login(request, user)
            return redirect('landing page')

        context = {
            'categories': Category.objects.all(),
            'form': SignUpForm(),
            'profile_form': ProfileForm()

        }
        return render(request, 'grocery/auth/sign_up.html', context)


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing page')

    else:
        form = SignInForm()

    context = {
        'categories': Category.objects.all(),
        'form': form,
    }

    return render(request, 'grocery/auth/sign_in.html', context)


@login_required
def sign_out(request):
    logout(request)
    return redirect('landing page')
