from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import UserViewSet, RecipeViewSet, FavoriteRecipeViewSet, ProfileView

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('recipes', RecipeViewSet)
router.register('favorites', FavoriteRecipeViewSet)
router.register('profile', ProfileView)

urlpatterns = [
    path('', include(router.urls))
]
