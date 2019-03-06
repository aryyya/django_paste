from .models import Paste
from .serializers import PasteSerializer

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

class PasteList(APIView):
    """
    List all pastes, or create a new paste.
    """
    def get(self, request, format=None):
        pastes = Paste.objects.all()
        serializer = PasteSerializer(pastes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PasteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PasteDetail(APIView):
    """
    Retrieve, update, or delete a paste instance.
    """

    def get_object(self, pk):
        try:
            return Paste.objects.get(pk=pk)
        except Paste.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        paste = self.get_object(pk)
        serializer = PasteSerializer(paste)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        paste = self.get_object(pk)
        serializer = PasteSerializer(paste, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None):
        paste = self.get_object(pk)
        paste.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
