from django.db import models

#Models: Ingredient, Recipe, RecipeIngredient, RecipeStep


class Ingredient(models.Model):
    # ex: salt, flour, ground beef
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """
    A list of recipes, consisting of both ingredients and steps.
    """
    MEAL_TYPES = (
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Dessert', 'Dessert'),
        ('Appetizer', 'Appetizer'),
        ('Snack', 'Snack'),
    )

    name = models.CharField(max_length=50)
    meal_type = models.CharField(max_length=50, choices=MEAL_TYPES)
    description = models.TextField()
    vegetarian = models.BooleanField(default=False)
    gluten_free = models.BooleanField(default=False)
    nut_free = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    """
    A list of ingredients used in a recipe.
    """
    UNITS_OF_MEASURE = (
        ('oz', 'oz'),
        ('cup', 'cup'),
        ('tsp', 'tsp'),
        ('TBSP', 'TBSP'),
        ('pinch', 'pinch'),
        ('lb', 'lb'),
        ('whole', 'whole'),
    )

    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredient)
    quantity = models.CharField(max_length=50)
    unit_of_measure = models.CharField(max_length=50, choices=UNITS_OF_MEASURE)

    def __str__(self):
        return '{0} {1} {2}'.format(self.quantity,
            self.unit_of_measure, self.ingredient
        )


class RecipeStep(models.Model):
    """
    A list of steps used in preparing a recipe.
    """
    recipe = models.ForeignKey(Recipe)
    sequence = models.PositiveSmallIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['sequence']
