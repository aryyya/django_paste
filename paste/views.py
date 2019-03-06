from .models import Paste
from .serializers import PasteSerializer

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def paste_list(request, format=None):
    """
    List all code pastes, or create a new paste.
    """
    if request.method == 'GET':
        pastes = Paste.objects.all()
        serializer = PasteSerializer(pastes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PasteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def paste_detail(request, pk, format=None):
    """
    Retrieve, update, or delete a code paste.
    """
    try:
        paste = Paste.objects.get(pk=pk)
    except Paste.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PasteSerializer(paste)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PasteSerializer(paste, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        paste.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
