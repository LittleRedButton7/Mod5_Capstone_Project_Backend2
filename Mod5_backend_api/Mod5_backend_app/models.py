from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class User(AbstractUser):
#     name = models.CharField(max_length=50, null=True)
    

#     def __str__(self):
#         return f'{self.id}: {self.username}'


class Recipe(models.Model):
    # recipe = models.TextField(max_length=300, blank=False, null=False)
    
    label = models.CharField(max_length=100, null=True)
    image = models.CharField(max_length=32, null=True)
    url = models.CharField(max_length=32, null=True)
    calories = models.CharField(max_length=32, default=0, null=True)
    carbs = models.CharField(max_length=32, null=True)
    protein = models.CharField(max_length=32, null=True)
    servings = models.CharField(max_length=32, null=True)

    def __str__(self):
        return f'{self.id}: {self.label}'
        # Do I need to add everything above here?

# Would I make a user model with a foreign key for the recipe book? Need to figure this out, then make migrations and then migrate to create relationship.
class FavoriteRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='favorites', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}: {self.recipe} {self.user}' 