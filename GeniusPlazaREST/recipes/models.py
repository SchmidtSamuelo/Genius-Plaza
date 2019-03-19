from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    dishName = models.CharField(max_length = 255)
    creator = models.ForeignKey(User, on_delete = CASCADE)