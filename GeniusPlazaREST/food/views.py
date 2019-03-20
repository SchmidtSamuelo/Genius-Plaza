from django.shortcuts import render
from .models import Recipe, Ingredient, Step
from django.http import HttpResponse

# Create your views here.

def recipes(request):
    return render(request, "Recipes/recipes.html")

def addRecipe(request):
    return HttpResponse('add')

def delRecipe(request, id):
    deleteRecipe = Recipe.objects.get(id = id)
    deleteRecipe.delete()





'''
old test APIs, probably not needed.

def addRecipe(request, recipeName, creatorName):
    rCreate = Recipe.objects.create(dishName = recipeName, recipeCreator = creatorName)
    rCreate.save()

def addIngredients(request, iName, recipeName, amount):
    iCreate = Ingredient.objects.create(ingredientName = iName, dishName = recipeName, amount = amount)
    iCreate.save()

def dictateSteps(request, recipeName, steps):
    sCreate = Step.objects.create(steps = steps, dishName = recipeName)
    sCreate.save()
'''