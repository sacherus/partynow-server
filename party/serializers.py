__author__ = 'sacherus'
from django.contrib.auth.models import User
from rest_framework import serializers
from models import Party


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ('id', 'title', 'start', 'end', 'organizers', 'participants',
                  'is_private', 'longitude', 'latitude')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


