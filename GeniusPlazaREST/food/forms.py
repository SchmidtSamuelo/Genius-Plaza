from django import forms
from food.models import Recipe

class recipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = '__all__'

class recipeDeleteForm(forms.ModelForm):
    
    class Meta:
        model = Recipe
        exclude = ('recipeCreator',)

#class stepCreateForm(forms.ModelForm):

    #class Meta:
        #model = 
        #fields = '__all__'