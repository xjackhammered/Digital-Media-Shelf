from django.urls import path
from . import views 

urlpatterns = [
    path('all-media/', views.medialist),
]
