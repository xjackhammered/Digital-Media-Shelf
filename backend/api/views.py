from django.shortcuts import render
from rest_framework.response import Response # pyright: ignore[reportMissingImports]
from rest_framework.decorators import api_view # pyright: ignore[reportMissingImports]
from .serializers import MediaSerializer, GenreSerializer, ReviewSerializer
from .models import MediaItem, Genre, Review
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

@api_view(['GET'])
def allGenres(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addGenre(request):
    serializer = GenreSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['POST', 'PATCH'])
def updateGenre(request, id):
    genre = Genre.objects.get(id=id)

    partial = request.method == 'PATCH'
    serializer = GenreSerializer(instance=genre, data=request.data, partial=partial)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteGenre(request, id):
    genre = Genre.objects.get(id=id)
    genre.delete()
    return Response("Genre has been successfully deleted!")

@api_view(['GET'])
def allReviews(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addReview(request):
    serializer = ReviewSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST', 'PATCH'])
def updateReview(request, id):
    review = Review.objects.get(id=id)

    partial = request.method == "PATCH"
    serializer = ReviewSerializer(instance=review, data=request.data, partial=partial)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteReview(request, id):
    review = Review.objects.get(id=id)
    review.delete()

    return Response("Review deleted successfully!")