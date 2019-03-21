from django.contrib import admin
from django.urls import path, include
from food import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.recipes, name='recipesHome'),
    url(r'^add_recipe/$', views.addRecipe, name='addRecipes'),
    url(r'^delete_recipe/$', views.delRecipe, name='delRecipes'),
]