from .models import Paste
from .serializers import PasteSerializer, UserSerializer

from django.contrib.auth.models import User

from rest_framework import generics

class PasteList(generics.ListCreateAPIView):
    queryset = Paste.objects.all()
    serializer_class = PasteSerializer

class PasteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paste.objects.all()
    serializer_class = PasteSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer