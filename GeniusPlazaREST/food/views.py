from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from django.views.generic import TemplateView
from food.forms import recipeCreationForm
from .models import Recipe, Ingredient, Step


# Create your views here.

# May not be needed after implimenting the classes
def recipes(request):
    return render(request, "recipes/recipes.html")

def addRecipe(request):
    return HttpResponse('add')

def delRecipe(request, id):
    deleteRecipe = Recipe.objects.get(id = id)
    deleteRecipe.delete()
# Above may not be needed after implimenting the classes

class recipesCreateTemplate(TemplateView):
    template_name = 'recipes/newrecipe.html'

    def get(self, request):
        hForm = recipeCreationForm()
        return render(request, self.template_name, {'form': hForm})
    def post(self, request):
        hForm = recipeCreationForm(request.POST)
        if hForm.is_valid():
            hForm.save()
        
        hForm = recipeCreationForm()
        args = {'form': hForm}
        return render(request, self.template_name, args)
