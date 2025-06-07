import requests
from recipe_finder.models import Recipe

API_KEY = "73ec19e9f63344b6beb1c232d6bc0a2a"  # Replace this with your actual key

def run():
    url = f"https://api.spoonacular.com/recipes/random"
    params = {
        "apiKey": API_KEY,
        "number": 1000
    }

    response = requests.get(url, params=params)
    data = response.json()

    for item in data.get("recipes", []):
        name = item.get("title")
        ingredients = [ing["name"] for ing in item.get("extendedIngredients", [])]
        ingredients_str = ", ".join(ingredients)
        instructions = item.get("instructions", "").strip()
        image = item.get("image", "")

        if name and ingredients_str:
            Recipe.objects.create(
                name=name,
                ingredients=ingredients_str,
                instructions=instructions,
                image_url=image
            )
            print(f"Added: {name}")

