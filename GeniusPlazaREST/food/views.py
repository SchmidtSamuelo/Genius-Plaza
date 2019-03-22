from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.views.generic.base import View
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from food.forms import recipeForm, recipeDeleteForm
from .models import Recipe, Ingredient, Step
from .serializers import UserSerializer, RecipeSerializer


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#must be CSRF Exempt
@csrf_exempt
def listRecipes(request):
#lists all recipes by default, allows the creation of a recipe
    if request.method == 'POST':
        #parses data from a json input, runs the serializer on it.
        data = JSONParser().parse(request)
        serializer = RecipeSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            #returns the saved data and a 201 (sucessful create) status code
            return JsonResponse(serializer.data, status = 201)

    elif request.method == 'GET':
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many = True)
        #returns serializer data, safe set to false. Must manually make
        #sure the JSON data is valid in the code.
        return JsonResponse(serializer.data, safe = False)

@csrf_exempt
def recipeDetail(request, pk):
    try:
        recipe = Recipe.objects.get(pk = pk)
    except Recipe.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RecipeSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            #returns the saved data
            return JsonResponse(serializer.data)

    elif request.method == 'GET':
        serializer = RecipeSerializer(recipe)
        return JsonResponse(serializer.data)
        
    elif request.method == 'DELETE':
        recipe.delete()
        #returns 204, sucessful delete
        return HttpResponse(status = 204)
        

#non_REST version to create a recipe. Functioning properly through HTML.
#Won't be narrating this block because it probably won't be used for the
#project
class RecipesCreateTemplate(TemplateView):
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

# Below may not be needed after implimenting the classes
#def recipes(request):
#    return render(request, "recipes/recipes.html")

#def addRecipe(request):
#    return HttpResponse('add')
# Above may not be needed after implimenting the classes

#non-REST version of delete. Does not have error catching
#will crash if an attempt to delete an object that doesn't
#exist is passed. Can be fixed by try/except 404.
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
