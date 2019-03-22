from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.base import View
from django.views.generic import TemplateView#, DeleteView
#from rest_framework.views import APIView
from food.forms import recipeForm, recipeDeleteForm
from .models import Recipe, Ingredient, Step


# Create your views here.

# May not be needed after implimenting the classes
def recipes(request):
    return render(request, "recipes/recipes.html")

def addRecipe(request):
    return HttpResponse('add')
# Above may not be needed after implimenting the classes

#class recipesView(APIView):
    #def get(self, request)

#class recipesAPIView(APIView):
    #pass 

'''
def recipeDelete(request, pk):
    template_name = 'recipes/deleterecipe.html'
    recipe = get_object_404(Recipe, pk=pk)
    if request.method == 'POST':
        dForm = recipeForm(request.POST, instance = recipe)
        recipe.delete()
    else:
        dForm = recipeForm(instance = recipe)
    
    args = {'form': dForm}
    return render(request, template, args)
'''

class recipesCreateTemplate(TemplateView):
    template_name = 'recipes/newrecipe.html'

    def get(self, request):
        hForm = recipeForm()
        return render(request, self.template_name, {'form': hForm})

    def post(self, request):
        hForm = recipeForm(request.POST)
        if hForm.is_valid():
            hForm.save()
            dName = hForm.cleaned_data['dishName']
            rCreator = hForm.cleaned_data['recipeCreator']
        
        hForm = recipeForm()
        args = {'form': hForm, 'dName': dName, 'rCreator': rCreator}
        return render(request, self.template_name, args)


#class stepsCreateTemplate(TemplateView):
#    template_name = 'recipes/createsteps.html'
# Unsure if needed, this isn't listed on the requirements. May include if I have time.


#failed attempts below, ask if possible
'''
class recipesDeleteTemplate(DeleteView):
    template_name = 'recipes/deleterecipe.html'

    def get(self, request):
        dForm = recipeDeleteForm()
        return render(request, self.template_name, {'form': dForm})

    def post(self, request):
        if request.method == 'POST':
            dForm = recipeForm()
            recipe = Recipe.objects.all()
            item_id = int(request.POST.get('item_id'))
            item = Recipe.objects.get(id = item_id)
            item.delete()

        dForm = recipeForm()
        args = {'form': dForm, 'recipe': recipe}
        return render(request, self.template_name, args)
'''