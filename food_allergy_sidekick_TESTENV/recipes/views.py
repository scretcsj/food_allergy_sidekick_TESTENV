from django.shortcuts import get_object_or_404, render, redirect
from .models import Recipe, KeyValueStore
from .forms import RecipeForm, RecipeSearchForm, KeyValueStoreForm, KeyValueStoreSearchForm
from django.conf import settings
from django.http import JsonResponse
import subprocess
import os


# Custom Recipes Views
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    ingredients = recipe.ingredients.split('\n') if recipe.ingredients else []
    instructions = recipe.instructions.split('\n') if recipe.instructions else []
    return render(request, 'recipe_detail.html', {
        'recipe': recipe,
        'ingredients': ingredients,
        'instructions': instructions,
    })


def search_recipes(request):
    if request.method == 'GET':
        form = RecipeSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Recipe.objects.filter(title__icontains=query)
            return render(request, 'recipe_search.html', {'form': form, 'results': results})
    else:
        form = RecipeSearchForm()
    return render(request, 'recipe_search.html', {'form': form})


def run_script(request):
    if request.method == "POST":
        ingredient = request.POST.get('ingredient')
        script_output = subprocess.check_output(['python', 'scripts/Test.py', ingredient], text=True)
        alternatives = script_output.splitlines()
        return JsonResponse({"script_output": alternatives})
    return JsonResponse({"message": "Invalid request"}, status=400)

# def run_script(request):
#     if request.method == "POST":
#         # Run your script and capture its output
#         script_output = subprocess.check_output(['python', 'scripts/Test.py'], text=True)
#         # Return the output as a JSON response
#         return JsonResponse({"script_output": script_output.splitlines()})
#     return JsonResponse({"message": "Invalid request"}, status=400)

# Sample Recipes .db views. rebuild each above if neccessary
# def recipe_list(request):
#     recipes = KeyValueStore.objects.all()
#     return render(request, 'recipe_list.html', {
#         'recipes': recipes,
#         })


# def recipe_detail(request, pk):
#     recipe = get_object_or_404(KeyValueStore, pk=pk)
#     # Removed split method becuase .db has one ingredient per column
#     ingredients = recipe.stringredient1
#     instructions = recipe.strinstructions.split('\r\n') if recipe.strinstructions else []
#     return render(request, 'recipe_detail.html', {
#         'recipe': recipe,
#         'ingredients': ingredients,
#         'instructions': instructions,
#     })


# def search_recipes(request):
#     if request.method == 'GET':
#         form = KeyValueStoreSearchForm(request.GET)
#         if form.is_valid():
#             query = form.cleaned_data['query']
#             results = KeyValueStore.objects.filter(strmeal__icontains=query)
#             return render(request, 'recipe_search.html', {'form': form, 'results': results})
#     else:
#         form = KeyValueStoreSearchForm()
#     return render(request, 'recipe_search.html', {'form': form})
