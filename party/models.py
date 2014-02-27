from django.db import models
import datetime
from gps.utils import haversine
# Create your models here.
from django.contrib.auth.models import User

class PartyManager(models.Manager):
    def in_area(self, kms, long, lat):
        return [party for party in self.all() if party.distance(long, lat) < kms]


class Party(models.Model):
    participants = models.ManyToManyField(User, blank=True, null=True, related_name="organize_party_set")
    organizers = models.ManyToManyField(User, blank=True, related_name="participate_party_set")
    start = models.DateTimeField(blank=True, null=True, )
    end = models.DateTimeField(blank=True, null=True)
    title = models.CharField(blank=True, max_length=255, default="Let's party now!")
    description = models.CharField(blank=True, null=True, max_length=1000, default="Example description")
    is_private = models.BooleanField(blank=True, default=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    objects = PartyManager()
    #where = models.FloatField()

    def distance(self, long, lat):
        if (self.longitude is None) or self.latitude is None:
            return float("inf")
        return haversine(self.longitude, self.latitude, long, lat)

    def __unicode__(self):
        return self.title


from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

#@receiver(post_save, sender=get_user_model())
#def create_auth_token(sender, instance=None, created=False, **kwargs):
#    if created:
#        Token.objects.create(user=instance)