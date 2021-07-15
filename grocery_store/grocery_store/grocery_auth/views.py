from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from grocery_store.grocery_auth.forms import SignInForm


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign in')
    else:
        form = UserCreationForm()

    context = {
        'form': form,
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
        'form': form,
    }

    return render(request, 'grocery/auth/sign_in.html', context)


# user = authenticate(username='dean', password='qwe123')
# login(request, user)
# return redirect('landing page')

@login_required
def sign_out(request):
    logout(request)
    return redirect('landing page')
