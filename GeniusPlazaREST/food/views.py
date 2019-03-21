from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from django.views.generic import TemplateView
from food.forms import recipeCreationForm
from .models import Recipe, Ingredient, Step


# Create your views here.

def recipes(request):
    return render(request, "recipes/recipes.html")

def addRecipe(request):
    return HttpResponse('add')

def delRecipe(request, id):
    deleteRecipe = Recipe.objects.get(id = id)
    deleteRecipe.delete()

class recipesHomeTemplate(TemplateView):
    template_name = 'recipes/recipes.html'

    def get(self, request):
        hForm = recipeCreationForm()
        return render(request, self.template_name, {'form': hForm})