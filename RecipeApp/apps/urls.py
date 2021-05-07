from django.urls import path

from RecipeApp.apps.views import indexView, searchByName, searchByIngredient,searchById, categories, searchByCategory

urlpatterns = [
    path('', indexView),
    path('searchByName/<query>/', searchByName),
    path('searchByIngredient/<query>/', searchByIngredient),
    path('searchById/<query>/', searchById),
    path('categories/', categories),
    path('searchByCategory/<query>/', searchByCategory)

]