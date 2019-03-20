from django.shortcuts import render
from rest_framework import viewsets
from .models import Recipe, Ingredient, Step
from .serializers import RecipeUpdateSerializer

# Create your views here.

class RecipesViews(viewsets.ModelViewSet):
    recipeObjects = Recipe.objects.all()
    recipeSerializer = RecipeUpdateSerializer