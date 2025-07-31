from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MediaSerializer, GenreSerializer, ReviewSerializer
from .models import MediaItem
# Create your views here.

@api_view(['GET'])
def medialist(request):
    medias = MediaItem.objects.all()
    serializer = MediaSerializer(medias, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addMedia(request):
    serializer = MediaSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteMedia(request, id):
    media = MediaItem.objects.get(id=id)
    media.delete()
    return Response("Media deleted successfully!")

@api_view(['POST', 'PATCH'])
def updateMedia(request, id):
    media = MediaItem.objects.get(id=id)

    partial = request.method == 'PATCH'
    serializer = MediaSerializer(instance=media, data=request.data, partial=partial)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


