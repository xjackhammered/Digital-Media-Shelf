from django.contrib import admin
from .models import MediaItem, Genre, Review
# Register your models here.
admin.site.register(MediaItem)
admin.site.register(Genre)
admin.site.register(Review)