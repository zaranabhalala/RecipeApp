from django.shortcuts import render
from django.http import HttpResponse
from django import template

import json
from django.views.decorators.csrf import csrf_exempt
import requests
#view for home page
def indexView(request):
    return render(request, 'index.html', {'all_ingredients': "test"})

#view for search recipe page
def searchView(request, recipeSearchName):
    try:
        url = f'https://www.themealdb.com/api/json/v1/1/search.php'
        params = {'s': recipeSearchName}
        r = requests.get(url=url, params=params)
        api_response = r.json()
        meals = []
        for meal in api_response['meals']:
            preprocess_fields = ['strMeal', 'strCategory', 'strArea', 'strInstructions', 'strYoutube', 'strTags']
            for field in preprocess_fields:
                if not(meal[field] is not None and meal[field] != ""):
                    meal[field] = "Information Not Available"

            ingredient_measure_list = []

            for i in range(1,21):
                ingredient_key = f'strIngredient{i}'
                measure_key = f'strMeasure{i}'
                if meal[ingredient_key] is not None and meal[ingredient_key] != "":
                    ingredient_measure_list.append([meal[ingredient_key], meal[measure_key]])
                del meal[ingredient_key]
                del meal[measure_key]

            meal['ingredient_measure_list'] = ingredient_measure_list
            meals.append(meal)
        response = {
            'recipeSearchName': recipeSearchName,
            'list_recipes': meals,
        }

    except:
        response = {'Error': 'No id with that name'}
    return render(request, 'searchRecipe.html', response)

