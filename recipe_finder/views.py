from django.shortcuts import render, redirect
from .models import Recipe, PantryItem

# Handles pantry management and searching
def index(request):
    action = request.GET.get('action')  # Determine what action user wants to perform

    if action == 'add':
        # Add a new pantry item entered by user
        ingredient = request.GET.get('pantry_item')
        if ingredient:
            PantryItem.objects.get_or_create(name=ingredient.strip())
            return redirect('/')  # Redirect to clear the query parameters

    elif action == 'delete':
        # Delete a pantry item specified by ID
        item_id = request.GET.get('item_id')
        PantryItem.objects.filter(id=item_id).delete()
        return redirect('/')  # Redirect to clear the query parameters

    elif action == 'search':
        # Search recipes using all pantry items as ingredients
        pantry_items = PantryItem.objects.values_list('name', flat=True)
        query = ",".join(pantry_items)
        return redirect(f'/results/?ingredients={query}')  # Redirect to results page with ingredients query

    # If no action, just show the current pantry
    pantry_items = PantryItem.objects.all()

    return render(request, 'recipe_finder/index.html', {
        'pantry_items': pantry_items
    })


# Handles displaying recipe search results based on ingredients query
def results(request):
    ingredients = request.GET.get('ingredients', '')
    # Create list of lowercased ingredients from the query string
    ingredients_list = [i.strip().lower() for i in ingredients.split(',') if i.strip()]

    matching_recipes = []
    for recipe in Recipe.objects.all():
        recipe_ingredients = recipe.ingredient_list()
        # Include recipe only if it contains all pantry ingredients
        if all(item in recipe_ingredients for item in ingredients_list):
            matching_recipes.append(recipe)

    return render(request, 'recipe_finder/results.html', {
        'ingredients': ingredients,
        'recipes': matching_recipes,
    })
