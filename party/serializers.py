__author__ = 'sacherus'

from rest_framework import serializers


class PartySerializer(serializers.Serializer):
    title = serializers.CharField(required=True,
                                  max_length=100)

