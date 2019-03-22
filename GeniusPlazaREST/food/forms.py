from django import forms
from food.models import Recipe

class recipeCreationForm(forms.ModelForm):
    #recipe_name = forms.CharField()
    #recipe_creator_username = forms.CharField()
    class Meta:
        model = Recipe
        fields = '__all__'
        # uncomment recipe_name and recipe_creator_username and
        # use fields = ('recipe_name', 'recipe_creator_username')
        # if '__all__' doesn't work

#class recipeDeleteForm(forms.ModelForm):
    #recipe_ID = forms.CharField()
    
    #class Meta:
        #model = 
        #fields = 'recipe_ID'

#class stepCreateForm(forms.ModelForm):

    #class Meta:
        #model = 
        #fields = '__all__'