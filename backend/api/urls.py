from django.urls import path
from . import views 

urlpatterns = [
    path('all-media/', views.medialist),
    path('add-media', views.addMedia),
    path('delete-media/<int:id>/', views.deleteMedia),
    path('update-media/<int:id>/', views.updateMedia),
    path('all-genre/', views.allGenres),
    path('add-genre/', views.addGenre),
    path('delete-genre/<int:id>/', views.deleteGenre),
    path('update-genre/<int:id>/', views.updateGenre),
]
