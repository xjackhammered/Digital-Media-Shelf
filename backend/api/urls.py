from django.urls import path
from . import views 

urlpatterns = [
    path('all-media/', views.medialist),
    path('add-media', views.addMedia),
    path('delete-media/<int:id>/', views.deleteMedia),
    path('update-media/<int:id>/', views.updateMedia),
]
