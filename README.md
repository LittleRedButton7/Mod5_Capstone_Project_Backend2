# In a Pinch
Make something with what you have in a pinch!


## Table of Contents
* [General Info](#General-Info)
* [Technologies](#Technologies)
* [Setup](#Setup)
* [Code Examples](#Code-Examples)
* [Features](#Features)
* [Status](#Status)
* [Contact](#Contact)

## General Info
I used an external recipe and nutrition API to pull in data on different recipes and include ingredients and nutrition. My thought was to make a website where you can put in a list of ingredients that you have on hand or need to use up and find recipes that match as well as meet your nutritional needs.

## Technologies
* Django
* SQLite3 - version 1.4
* React
* HTML
* CSS


## Setup
* This is the backend repo. The frontend repo can be found [here](https://github.com/LittleRedButton7/Mod5_Capstone_Project_Frontend)  
* Fork and clone this repo into your local branch.
* From the backend, open up the api and activate with source venv/bin/activate. 
* Then enter into the Mod5_backend_api and run python manage.py runserver to kick off the server.
* Open in VS code or other text editor if you'd like to see the code.
* Fork and clone the front end. Open it and run the frontend with npm start.
* From there, create an account, login and have fun looking up recipes for ingredients that you have on hand. Note that you can see a list of all the ingredients on the back of the recipe cards.
* You can also save a recipe to your recipe book to find later. 

## Code Examples
Django Model
```
class FavoriteRecipe(models.Model):
    recipebook = models.ForeignKey(RecipeBook, related_name='favorites', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}: {self.recipebook} {self.user}' 
```

Django Views
```
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserSerializer, RecipeBookSerializer, FavoriteRecipeSerializer
from .models import RecipeBook, FavoriteRecipe

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RecipeBookViewSet(viewsets.ModelViewSet):
    queryset = RecipeBook.objects.all()
    serializer_class = RecipeBookSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
        
```

Django Serializers
```
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import RecipeBook, FavoriteRecipe

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class RecipeBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeBook
        fields = ['id', 'recipe']
```

## Features
* Register as a new user and Login are both connected to the Django backend's authentication.
    * If you try to login with a username that's already taken, an alert will pop up on the frontend letting you know you need to pick a different username/login.
    * If you enter an incorrect password on the login page, an alert on the frontend will let you know the login was unsuccessful. 
* Recipe search function allows you to search by ingredients that you have on hand and returns a list of results.     
    * Each recipe card flips and you can see a full list of ingredients. This was designed as such because that way you can tell if you have everything without having to open the full link. This is an effort to make selecting a recipe you can make with what you have easier and quicker to find.
    * Also on the back of the card is an option to save the recipe to your recipe book. There is a link at the top that will take you to your saved recipes for reference later. 
    * Additionally, there is a link on the back of the recipe card that will take you to the full recipe. This is an external link.

## Status
This is a full stack, functioning app. However, at the moment you have to fork and clone both the frontend and the backend to get it working correctly. Eventually, I would like to deploy this live so people can access it through a functioning URL.

## Contact
Feel free to reach out and connect with me!
[Marissa Nolan](https://www.linkedin.com/in/marissanolan1/) 

### Thanks for visiting!
