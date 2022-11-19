from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from .models import User, UserProfile

@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except ObjectDoesNotExist: # Not sure if right yet
            # create the userprofile if not exist
            UserProfile.objects.create(user=instance)
        # run if user is updated

# Using decorator instead
# post_save.connect(post_save_create_profile_receiver, sender=User)