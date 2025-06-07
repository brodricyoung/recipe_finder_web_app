import requests
from recipe_finder.models import Recipe

API_KEY = "73ec19e9f63344b6beb1c232d6bc0a2a"  # Spoonacular API key (replace with your own)

def run():
    url = f"https://api.spoonacular.com/recipes/random"
    params = {
        "apiKey": API_KEY,
        "number": 1000  # Request 1000 random recipes (may be rate limited)
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Iterate through each recipe returned by the API
    for item in data.get("recipes", []):
        name = item.get("title")
        # Extract ingredient names from the extendedIngredients field
        ingredients = [ing["name"] for ing in item.get("extendedIngredients", [])]
        ingredients_str = ", ".join(ingredients)
        instructions = item.get("instructions", "").strip()
        image = item.get("image", "")

        # Create a Recipe record if name and ingredients are valid
        if name and ingredients_str:
            Recipe.objects.create(
                name=name,
                ingredients=ingredients_str,
                instructions=instructions,
                image_url=image
            )
            print(f"Added: {name}")
