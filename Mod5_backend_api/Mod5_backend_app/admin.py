from django.contrib import admin
from .models import Recipe, FavoriteRecipe
# Register your models here.
admin.site.register(Recipe)
admin.site.register(FavoriteRecipe)
