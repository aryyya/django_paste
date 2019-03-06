from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Paste
from .serializers import PasteSerializer
from rest_framework.status import *

@csrf_exempt
def paste_list(request):
    """
    List all code paste, or create a new paste.
    """
    if request.method == 'GET':
        pastes = Paste.objects.all()
        serializer = PasteSerializer(pastes, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PasteSerializer(data=data)
        if (serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

@csrf_exempt
def paste_detail(request, pk):
    """
    Retrieve, update, or delete a code paste.
    """
    try:
        paste = Paste.objects.get(pk=pk)
    except Paste.DoesNotExist:
        return HttpResponse(status=HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PasteSerializer(paste)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PasteSerializer(paste, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        paste.delete()
        return HttpResponse(status=HTTP_204_NO_CONTENT)
