from django.shortcuts import render
from rest_framework.response import Response # pyright: ignore[reportMissingImports]
from rest_framework.decorators import api_view, permission_classes # pyright: ignore[reportMissingImports]
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import MediaSerializer, GenreSerializer, ReviewSerializer, RegisterSerializer
from .models import MediaItem, Genre, Review

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"User Registered!"}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"message":"Logged out"})
    except Exception:
        return Response({"error":"Invalid Token"}, status=400)


@api_view(['GET'])
def medialist(request):
    medias = MediaItem.objects.all()
    serializer = MediaSerializer(medias, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addMedia(request):
    serializer = MediaSerializer(data=request.data)

    if serializer.is_valid():
        media = serializer.save(owner=request.user)
        return Response(MediaSerializer(media).data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteMedia(request, id):
    try:
        media = MediaItem.objects.get(id=id, owner=request.user)
    except MediaItem.DoesNotExist:
        return Response({"error":"Not found or not allowed"}, status=404)
    
    media.delete()
    return Response({"message": "Media deleted successfully!"})

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def updateMedia(request, id):
    try:
        media = MediaItem.objects.get(id=id, owner=request.user)
    except MediaItem.DoesNotExist:
        return Response({"error": "Not found or not allowed"}, status=404)

    serializer = MediaSerializer(media, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)

@api_view(['GET'])
def allGenres(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addGenre(request):
    serializer = GenreSerializer(data=request.data)

    if serializer.is_valid():
        genre = serializer.save()
        return Response(GenreSerializer(genre).data, status=201)
    
    return Response(serializer.errors, status=400)

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
@permission_classes([IsAuthenticated])
def addReview(request):
    
    serializer = ReviewSerializer(data=request.data)

    if serializer.is_valid():
        review = serializer.save(owner=request.user)
        return Response(ReviewSerializer(review).data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def updateReview(request, id):
    try:
        review = Review.objects.get(id=id, owner=request.user)
    except Review.DoesNotExist:
        return Response({"error":"Not found or not allowed"},status=404)
    
    serializer = ReviewSerializer(review, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)    
    
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteReview(request, id):
    review = Review.objects.get(id=id, owner=request.user)
    review.delete()
    return Response("Review deleted successfully!")