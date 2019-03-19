from django.db import models

# Create your models here.

class Recipe(models.Model):
    dishName = models.CharField(max_length = 255)
    creatorEmail = models.CharField(max_length = 255)