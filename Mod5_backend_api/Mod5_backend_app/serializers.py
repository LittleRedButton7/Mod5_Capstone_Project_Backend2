from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from .models import RecipeBook, FavoriteRecipe

class UserObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class RecipeBookObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeBook
        fields = '__all__'

class FavoriteRecipeObjectSerializer(serializers.ModelSerializer):
    recipebook = RecipeBookObjectSerializer(many=False)

    class Meta:
        model = FavoriteRecipe
        fields = ['id', 'recipebook', 'user']

class UserSerializer(serializers.ModelSerializer):
    favorite_recipes = FavoriteRecipeObjectSerializer(many=True, required=False)
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'favorite_recipes']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user_password = validated_data.pop('password')
        user = User.objects.create(
            **validated_data,
            password = make_password(user_password)
        )
        user.save()
        Token.objects.create(user=user)
        return user

class RecipeBookSerializer(serializers.ModelSerializer):
    users = UserObjectSerializer(many=True, read_only=True)
    favorite_recipes = FavoriteRecipeObjectSerializer(many=True, read_only=True)
    
    class Meta:
        model = RecipeBook
        fields = ['id', 'recipe', 'users', 'favorite_recipes']

class FavoriteRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteRecipe
        fields = ['id', 'recipebook', 'user']

# image','label', 'url', 'calories', 'carbs', 'protein', 'servings