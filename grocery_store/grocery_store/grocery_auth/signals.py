from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from grocery_store.profiles.models import Profile, ProfileAddress

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    if created:
        profile = Profile(
            user=instance,
        )
        address = ProfileAddress(
            profile=profile,
        )

        profile.save()
        address.save()