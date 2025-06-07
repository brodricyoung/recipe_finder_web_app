from django.shortcuts import render, redirect
from .models import Recipe
from .models import PantryItem

# Create your views here.
def index(request):
    action = request.GET.get('action')

    if action == 'add':
        ingredient = request.GET.get('pantry_item')
        if ingredient:
            PantryItem.objects.get_or_create(name=ingredient.strip())
            return redirect('/')  # clean URL

    elif action == 'delete':
        item_id = request.GET.get('item_id')
        PantryItem.objects.filter(id=item_id).delete()
        return redirect('/')  # clean URL

    elif action == 'search':
        pantry_items = PantryItem.objects.values_list('name', flat=True)
        query = ",".join(pantry_items)
        return redirect(f'/results/?ingredients={query}')

    pantry_items = PantryItem.objects.all()

    return render(request, 'recipe_finder/index.html', {
        'pantry_items': pantry_items
    })


def results(request):
    ingredients = request.GET.get('ingredients', '')
    ingredients_list = [i.strip().lower() for i in ingredients.split(',') if i.strip()]

    matching_recipes = []
    for recipe in Recipe.objects.all():
        recipe_ingredients = recipe.ingredient_list()
        if all(item in recipe_ingredients for item in ingredients_list):
            matching_recipes.append(recipe)

    return render(request, 'recipe_finder/results.html', {
        'ingredients': ingredients,
        'recipes': matching_recipes,
    })
