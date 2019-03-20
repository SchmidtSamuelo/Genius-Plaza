from django.urls import path, include
from food import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('food', views.RecipesViews, 'Recipe')

urlpatterns = [
    path('', include(router.urls))
]