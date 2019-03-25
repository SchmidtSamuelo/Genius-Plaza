from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import User
from .models import Recipe, Ingredient, Step

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class RecipeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(required = False, allow_blank = True)
    recipe_reator = serializers.CharField(required = False)

    def create(self, validated_data):
        return Recipe.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.recipeCreator = validated_data.get('recipeCreator', instance.recipeCreator)
        instance.save()
        return instance
    class Meta:
        model = Recipe
        fields = ('id' ,'name', 'recipe_creator')
