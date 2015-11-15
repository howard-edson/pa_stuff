#from django.shortcuts import render
from django.views import generic
from .models import Ingredient, Recipe #, RecipeIngredient, RecipeStep

class RecipeList(generic.ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    # the automatically generated context variable is recipe_list

class IngredientList(generic.ListView):
    model = Ingredient
    template_name = 'recipes/ingredient_list.html'
    # the automatically generated context variable is ingredient_list
