from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views 

urlpatterns = [
    path("register/",views.register, name="register"),
    path("login/",TokenObtainPairView.as_view(), name="login"),
    path("refresh/",TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/",views.logout, name="logout"),
    
    path('all-media/', views.medialist),
    path('add-media', views.addMedia),
    path('delete-media/<int:id>/', views.deleteMedia),
    path('update-media/<int:id>/', views.updateMedia),
    path('all-genre/', views.allGenres),
    path('add-genre/', views.addGenre),
    path('delete-genre/<int:id>/', views.deleteGenre),
    path('update-genre/<int:id>/', views.updateGenre),
    path('all-review/', views.allReviews),
    path('add-review/', views.addReview),
    path('delete-review/<int:id>/', views.deleteReview),
    path('update-review/<int:id>/', views.updateReview),
]