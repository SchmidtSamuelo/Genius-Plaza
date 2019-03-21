from django import forms

class recipeCreationForm(forms.Form):
    recipeName = forms.CharField()
    recipeCreator = forms.CharField()