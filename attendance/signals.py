from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Athlete

@receiver(post_save, sender=User)
def create_athlete(sender, instance, created, **kwargs):
    if created:
        Athlete.objects.create(user=instance)