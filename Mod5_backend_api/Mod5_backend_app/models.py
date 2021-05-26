from django.db import models
from django.contrib.auth.models import User

class RecipeBook(models.Model):
    recipe = models.TextField(max_length=300, blank=False, null=False)
    users = models.ManyToManyField(User, related_name='users', through='FavoriteRecipe')
    # label = models.TextField(max_length=100, blank=False, null=False)
    # image = models.TextField(max_length=32, blank=False, null=False)
    # url = models.TextField(max_length=32, blank=False, null=False)
    # calories = models.IntegerField(default=0,blank=False, null=False)
    # carbs = models.IntegerField(blank=False, null=False)
    # protein = models.IntegerField(blank=False, null=False)
    # servings = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return f'{self.id}: {self.recipe}'
        # Do I need to add everything above here?


# Would I make a user model with a foreign key for the recipe book? Need to figure this out, then make migrations and then migrate to create relationship.
class FavoriteRecipe(models.Model):
    recipebook = models.ForeignKey(RecipeBook, blank=True, null=True, related_name='favorite_recipes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, null=True, related_name='favorite_recipes', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}: {self.user.username} likes {self.recipe.name}'
