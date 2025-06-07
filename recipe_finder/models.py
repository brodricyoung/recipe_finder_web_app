from django.db import models

# Model to represent a Recipe with its attributes
class Recipe(models.Model):
    name = models.CharField(max_length=100)  # Recipe title
    ingredients = models.TextField(help_text="Comma-separated list of ingredients")  # Ingredients stored as a string
    instructions = models.TextField(blank=True)  # Optional cooking instructions
    image_url = models.URLField(blank=True)  # Optional URL for recipe image

    def __str__(self):
        return self.name  # Display recipe name in admin and shell

    def ingredient_list(self):
        # Returns a list of lowercase ingredient names from the comma-separated string
        return [i.strip().lower() for i in self.ingredients.split(',') if i.strip()]


# Model to represent an ingredient saved by the user in their pantry
class PantryItem(models.Model):
    name = models.CharField(max_length=100)  # Ingredient name

    def __str__(self):
        return self.name  # Display ingredient name in admin and shell
