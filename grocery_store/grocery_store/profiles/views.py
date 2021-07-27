from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.db import transaction
from django.shortcuts import render, redirect
from grocery_store.grocery_auth.forms import SignUpForm, EditUserForm
from grocery_store.profiles.forms import ProfileForm
from grocery_store.profiles.models import Profile


@login_required
@transaction.atomic
def edit_profile(request):
    if request.method == 'GET':
        context = {
            'user_form': EditUserForm(instance=request.user),
            'profile_form': ProfileForm(instance=Profile.objects.get(pk=request.user.pk)),
        }
        return render(request, 'grocery/profile/edit-profile.html', context)

    else:
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=Profile.objects.get(pk=request.user.id))

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile details')

        context = {
            'user_form': EditUserForm(instance=request.user),
            'profile_form': ProfileForm(instance=Profile.objects.get(pk=request.user.pk)),
        }
        return render(request, 'grocery/profile/edit-profile.html', context)


@login_required
def profile_details(request):
    profile = Profile.objects.get(pk=request.user.pk)

    context = {
        'grocery_user': request.user,
        'profile': profile,
    }

    return render(request, 'grocery/profile/profile_details.html', context)


class ChangePasswordView(PasswordChangeView):
    def get_form(self, **kwargs):
        form = super().get_form(**kwargs)
        self.__apply_bootstrap_classes(form)
        return form

    def __apply_bootstrap_classes(self, form):
        for (_, field) in form.fields.items():
            field.widget.attrs = {
                'class': 'form-control',
            }

    template_name = 'grocery/profile/change_password.html'
    success_url = '/'
