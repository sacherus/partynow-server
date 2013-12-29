from django.db import models


# Create your models here.
from django.contrib.auth.models import User


class Party(models.Model):
    #participants = models.ManyToManyField(User)
    #organizers = models.ManyToManyField(User)
    start = models.DateField()
    end = models.DateField()
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title