from .models import MediaItem, Genre, Review
from rest_framework import serializers


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        

class ReviewSerializer(serializers.ModelSerializer):
    media = serializers.StringRelatedField(read_only=True)

    media_id = serializers.PrimaryKeyRelatedField(
        queryset = MediaItem.objects.all(),
        write_only = True,
        source = 'media'
    )

    class Meta:
        model = Review
        fields = ['id', 'content', 'rating', 'created_at', 'media', 'media_id']


class MediaSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)

    genre_ids = serializers.PrimaryKeyRelatedField(
        queryset = Genre.objects.all(),
        many = True,
        write_only = True,
        source = 'genres'
    )
    
    reviews = ReviewSerializer(read_only=True, many=True)
    
    class Meta:
        model = MediaItem
        fields = ['name','type','genres','status', 'created_at', 'genre_ids', 'reviews' ]

