from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
from party.models import Party
from party.serializers import PartySerializer, UserSerializer
from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def index(request):
    output="Hello2"
    return HttpResponse(output)


class PartyList(generics.ListCreateAPIView):
    serializer_class = PartySerializer

    def get_queryset(self):
        if "area" in self.request.GET:
            area = float(self.request.GET["area"])
            long = float(self.request.GET["longitude"])
            lat = float(self.request.GET["latitude"])
            queryset = Party.objects.in_area(area, long, lat)
        else:
            queryset = Party.objects.all()
        return queryset

    def post_save(self, obj, created):
        obj.organizers.add(self.request.user)
        obj.save()

class PartyDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Party
    serializer_class = PartySerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = (permissions.IsAuthenticated,)

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['POST'])
def create_auth(request):
    serialized = UserSerializer(data=request.DATA)
    if serialized.is_valid():
        User.objects.create_user(
            #serialized.init_data['email'],
            serialized.init_data['username'],
            serialized.init_data['password']
        )
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)