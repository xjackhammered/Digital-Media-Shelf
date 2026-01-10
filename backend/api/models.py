from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MediaItem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="media", null=True, blank=True)
    MEDIA_TYPES = [('movie', 'Movie'),
                   ('game', 'Game'),
                   ('series', 'Series'),
                   ('book', 'Book')]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    genres = models.ManyToManyField('Genre', blank=False)
    status = models.CharField(choices=[
        ('completed', 'Completed'),
        ('watching', 'Watching'),
        ('wishlisted', 'Wishlisted'),
        ('dropped', 'Dropped')
    ], max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Review(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review", null=True, blank=True)
    media = models.ForeignKey(MediaItem, on_delete=models.CASCADE, related_name="reviews")
    content = models.TextField(max_length=100, null=False)
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[0:50]