from django.contrib import admin
from django.urls import path, include
from food import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.recipesCreateTemplate.as_view(), name='recipesHome'),
    #url(r'^delete_recipe/$', views.recipesDeleteTemplate.as_view(), name='delRecipes'),
]