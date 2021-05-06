from django.urls import path

from RecipeApp.apps.views import indexView, searchView

urlpatterns = [
    path('', indexView),
    path('search/<recipeSearchName>/', searchView)
]