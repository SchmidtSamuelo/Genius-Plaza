from django import forms
from food.models import Recipe

class recipeCreationForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = '__all__'

#class recipeDeleteForm(forms.ModelForm):
    #recipe_ID = forms.CharField()
    
    #class Meta:
        #model = 
        #fields = 'recipe_ID'

#class stepCreateForm(forms.ModelForm):

    #class Meta:
        #model = 
        #fields = '__all__'