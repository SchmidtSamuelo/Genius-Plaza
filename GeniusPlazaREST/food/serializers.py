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
    dishName = serializers.CharField(required = False, allow_blank = True)
    rCreator = serializers.CharField(required = False)

    def create(self, validated_data):
        return Recipe.objects.create(**validated_data)

    def update(self, validated_data):
        instance.dishName = validated_data.get('dishName', instance.dishName)
        instance.recipeCreator = validated_data.get('recipeCreator', instance.recipeCreator)
        instance.save()
        return instance
    class Meta:
        model = Recipe
        fields = ('id' ,'dishName', 'rCreator')
