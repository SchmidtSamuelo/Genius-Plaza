from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    dishName = models.CharField(max_length = 255)
    recipeCreator = models.ForeignKey(User, on_delete = models.CASCADE, null=True, default = 0, related_name='creator')
    def __str__(self):
        return self.dishName

class Ingredient(models.Model):
    ingredientName = models.CharField(max_length=255)
    amount = models.CharField(max_length=63)
    dishName = models.ForeignKey(Recipe, on_delete = models.CASCADE, default = "0")
    def __str__(self):
        return self.ingredientName

class Step(models.Model):
    dishName = models.ForeignKey(Recipe, on_delete = models.CASCADE, default = "0")
    stepNumber = models.IntegerField()
    stepDescription = models.TextField()
    def __str__(self):
        return self.dishName