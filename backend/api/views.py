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