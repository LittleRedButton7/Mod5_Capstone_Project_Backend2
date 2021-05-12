from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RecipeBook(models.Model):
    recipe = models.TextField(max_length=300, blank=False, null=False)
    
    # label = models.TextField(max_length=100, blank=False, null=False)
    # image = models.TextField(max_length=32, blank=False, null=False)
    # url = models.TextField(max_length=32, blank=False, null=False)
    # calories = models.IntegerField(default=0,blank=False, null=False)
    # carbs = models.IntegerField(blank=False, null=False)
    # protein = models.IntegerField(blank=False, null=False)
    # servings = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return f'{self.id}: {self.label}'
        # Do I need to add everything above here?

# Would I make a user model with a foreign key for the recipe book? Need to figure this out, then make migrations and then migrate to create relationship.
class FavoriteRecipe(models.Model):
    recipebook = models.ForeignKey(RecipeBook, related_name='favorites', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}: {self.recipebook} {self.user}' 