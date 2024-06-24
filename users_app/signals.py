from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from .models import CustomUser, Profile, MentorProfile, MenteeProfile


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'mentor':
            MentorProfile.objects.create(user=instance)
        elif instance.role == 'mentee':
            MenteeProfile.objects.create(user=instance)
