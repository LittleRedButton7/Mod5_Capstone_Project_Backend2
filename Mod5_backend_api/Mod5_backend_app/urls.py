from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import UserViewSet, RecipeBookViewSet, FavoriteRecipeViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('recipebooks', RecipeBookViewSet)
router.register('favorites', FavoriteRecipeViewSet)

urlpatterns = [
    path('', include(router.urls))
]
