from .models import Paste
from .serializers import PasteSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly

from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    print('api_root()')
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'pastes': reverse('paste-list', request=request, format=format)
    })

class PasteList(generics.ListCreateAPIView):
    queryset = Paste.objects.all()
    serializer_class = PasteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PasteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paste.objects.all()
    serializer_class = PasteSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )

class PasteHighlight(generics.GenericAPIView):
    queryset = Paste.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        paste = self.get_object()
        return Response(paste.highlighted)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
