from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, ProviderProfile, SeekerProfile

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.type == User.Types.PROVIDER:
            ProviderProfile.objects.get_or_create(user=instance)
        elif instance.type == User.Types.SEEKER:
            SeekerProfile.objects.get_or_create(user=instance)