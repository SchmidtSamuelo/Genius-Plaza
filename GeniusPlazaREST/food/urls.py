from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from food import views

urlpatterns = [
    url(r'^$', views.RecipesCreateTemplate.as_view(), name='recipesHome'),
    path('modify_recipes/', views.listRecipes),
    path('modify_recipes/<int:pk>/', views.recipeDetail),    
    #url(r'^delete_recipe/$', views.recipesDeleteTemplate.as_view(), name='delRecipes'),
]
