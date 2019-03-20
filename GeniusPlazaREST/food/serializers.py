from rest_framework import serializers
from .models import Recipe, Ingredient, Step

class RecipeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('dishName', 'recipeCreator')