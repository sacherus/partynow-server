from django.db import models
import datetime

# Create your models here.
from django.contrib.auth.models import User


class Party(models.Model):
    participants = models.ManyToManyField(User, blank=True, null=True, related_name="organize_party_set")
    organizers = models.ManyToManyField(User, blank=True, related_name="participate_party_set")
    start = models.DateField(auto_now_add=True, blank=True)
    end = models.DateField(blank=True, null=True)
    title = models.CharField(blank=True, max_length=255, default="Let's party now!")
    is_private = models.BooleanField(blank=True, default=False)
    #where = models.FloatField()

    def __unicode__(self):
        return self.title


from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=get_user_model())
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)