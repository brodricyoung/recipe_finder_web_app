from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField(help_text="Comma-separated list of ingredients")
    instructions = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name
    
    def ingredient_list(self):
        return [i.strip().lower() for i in self.ingredients.split(',') if i.strip()]
    

class PantryItem(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name