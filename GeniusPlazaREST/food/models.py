from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ingredient(models.Model):
    text = models.CharField(max_length=255)
    def __str__(self):
        return self.text

class Step(models.Model):
    step_text = models.TextField()
    def __str__(self):
        return self.step_text

class Recipe(models.Model):
    name = models.CharField(max_length = 255, null=False)
    recipe_creator = models.ForeignKey(User, on_delete = models.CASCADE, null=True, default = 0, related_name='creator')
    step = models.ForeignKey(Step, on_delete = models.CASCADE, null=True, default = 0, related_name='steps')
    ingredient = models.ForeignKey(Ingredient, on_delete = models.CASCADE, null = True, default = 0, related_name = 'ingredents')
    def __str__(self):
        return self.name