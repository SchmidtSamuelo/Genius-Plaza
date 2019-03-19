from django.db import models
from recipes.models import Recipe

# Create your models here.

class Ingredient(models.Model):
    ingredientName = models.CharField(max_length=255)
    amount = models.CharField(max_length=63)
