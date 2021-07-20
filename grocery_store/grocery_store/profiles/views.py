from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from grocery_store.grocery_auth.forms import SignUpForm
from grocery_store.profiles.forms import ProfileForm, EditProfileForm
from grocery_store.profiles.models import Profile


@login_required
def edit_profile(request):

    if request.method == 'GET':
        context = {
            'user_form': EditProfileForm(instance=request.user),
            'profile_form': ProfileForm(instance=Profile.objects.get(pk=request.user.pk)),
        }

        return render(request, 'grocery/edit-profile.html', context)

    else:

        user_form = EditProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=Profile.objects.get(pk=request.user.id))

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('landing page')

        context = {
            'user_form': EditProfileForm(instance=request.user),
            'profile_form': ProfileForm(instance=Profile.objects.get(pk=request.user.pk)),
        }
        return render(request, 'grocery/edit-product.html', context)
