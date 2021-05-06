from django.urls import path

from ingredient.views import indexView, searchView

urlpatterns = [
    path('', indexView),
    path('search/<recipeSearchName>/', searchView)
]