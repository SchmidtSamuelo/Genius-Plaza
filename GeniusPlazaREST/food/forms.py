from django import forms

class HomeForm(forms.Form):
    recipeName = forms.CharField()
    #recipeCreator = forms.CharField(max_length = 63)