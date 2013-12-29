from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from party.models import Party
from party.serializers import PartySerializer, UserSerializer
from rest_framework import generics


def index(request):
    output="Hello"
    return HttpResponse(output)


class PartyList(generics.ListCreateAPIView):
    model = Party
    serializer_class = PartySerializer


class PartyDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Party
    serializer_class = PartySerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
