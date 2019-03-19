from django.db import models
from recipes.models import Recipe

# Create your models here.

class Step(models.Model):
    dishName = models.CharField(max_length = 255)
    stepNumber = models.IntegerField()
    stepDescription = models.TextField()