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
def searchByName(request, query):
    try:
        url = f'https://www.themealdb.com/api/json/v1/1/search.php'
        params = {'s': query}
        r = requests.get(url=url, params=params)
        api_response = r.json()
        print(api_response)

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
            'recipeSearchName': query,
            'list_recipes': meals,
        }

    except:
        response = {'Error': 'No id with that name'}
    return render(request, 'searchRecipeName.html', response)

def searchByIngredient(request, query):
    try:
        url = f'https://www.themealdb.com/api/json/v1/1/filter.php'
        params = {'i': query}

        r = requests.get(url=url, params=params)
        api_response = r.json()
        print(api_response)

        response = {
            'recipeSearchName': query,
            'list_recipes': api_response['meals'],
        }

    except:
        response = {'Error': 'No id with that name'}
    return render(request, 'searchRecipeIngredients.html', response)


def searchById(request, query):
    print("id", query)
    try:
        url = f'https://www.themealdb.com/api/json/v1/1/lookup.php'
        params = {'i': query}
        r = requests.get(url=url, params=params)
        print(r)
        api_response = r.json()
        print(api_response)

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
            'recipeSearchName': query,
            'list_recipes': meals,
        }

    except:
        response = {'Error': 'No id with that name'}
    return render(request, 'singleRecipe.html', response)



def categories(request):
    try:
        url = f'https://www.themealdb.com/api/json/v1/1/categories.php'
        r = requests.get(url=url)
        api_response = r.json()

        response = {
            'list_recipes': api_response['categories']
        }

    except:
        response = {'Error': 'No id with that name'}
    return render(request, 'categories.html', response)


def categories(request):
    try:
        url = f'https://www.themealdb.com/api/json/v1/1/categories.php'
        r = requests.get(url=url)
        api_response = r.json()

        response = {
            'list_recipes': api_response['categories']
        }

    except:
        response = {'Error': 'No id with that name'}
    return render(request, 'categories.html', response)

def searchByCategory(request, query):
    url = f'https://www.themealdb.com/api/json/v1/1/filter.php'
    params = {'c': query}

    r = requests.get(url=url, params=params)
    api_response = r.json()
    print(api_response)

    response = {
        'recipeSearchName': query,
        'list_recipes': api_response['meals'],
    }

    # except:
    #     response = {'Error': 'No id with that name'}
    return render(request, 'searchRecipeIngredients.html', response)