from django.shortcuts import get_object_or_404, render, redirect
from .models import Recipe
from .forms import RecipeForm, RecipeSearchForm


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
