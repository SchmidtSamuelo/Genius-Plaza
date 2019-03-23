from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import Recipe, Ingredient, Step
from .serializers import UserSerializer, RecipeSerializer


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET', 'POST'])
def listRecipes(request):
    #retrieves and lists the objects (defaults to all objects)
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many = True)
        #returns serializer data
        return Response(serializer.data)

    #creates new recipe
    elif request.method == 'POST':
        serializer = RecipeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            #returns the saved data and a 201 (sucessful create) status code
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'GET', 'DELETE'])
def recipeDetail(request, pk):
    try:
        recipe = Recipe.objects.get(pk = pk)
    except Recipe.DoesNotExist:
        return HttpResponse(status = status.HTTP_404_NOT_FOUND)

    #update recipes
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RecipeSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            #returns the saved data
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    #retrieve recipes
    elif request.method == 'GET':
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    #delete recipes    
    elif request.method == 'DELETE':
        recipe.delete()
        #returns 204, sucessful delete
        return Response(status = status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def listRecipesByUser(request):
    #retrieves recipes by recipe creator. Takes a username instead of a
    #first/last name input to streamline it a little more.
    if request.method == 'GET':
        recipes = Recipe.objects.all(recipeCreator = request.recipeCreator)
        serializer = RecipeSerializer(recipes, many = True)
        return Response(serializer.data)


#non_REST version to create a recipe. Functioning properly through HTML.
#Won't be narrating this block because it probably won't be used for the
#project
'''
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
'''
#non-REST version of delete. Does not have error catching
#will crash if there is an attempt to delete an object that doesn't
#exist. Can be fixed by try/except 404.
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
