from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import UserViewSet, RecipeBookViewSet, FavoriteRecipeViewSet, ProfileViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('recipebooks', RecipeBookViewSet)
router.register('favorite_recipes', FavoriteRecipeViewSet)
router.register('profile', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls))
]
