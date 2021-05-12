from django.contrib import admin
from .models import RecipeBook, FavoriteRecipe
# Register your models here.
admin.site.register(RecipeBook)
admin.site.register(FavoriteRecipe)
