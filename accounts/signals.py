from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print('Received signal for user:', instance)
    if created:
        print('Creating profile for user:', instance)
        Profile.objects.create(user=instance)
