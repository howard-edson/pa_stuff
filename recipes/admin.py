from django.contrib import admin
from django.db import models
from django.forms import TextInput
from .models import Ingredient, Recipe, RecipeIngredient, RecipeStep


class IngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 0
    # make sure inputs aren't too long in the admin site
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'10'})},
    }


class StepInline(admin.TabularInline):
    model = RecipeStep
    extra = 0
    # make sure inputs aren't too long in the admin site
    formfield_overrides = {
        models.TextField: {'widget': TextInput(attrs={'size':'100'})},
        models.PositiveSmallIntegerField: {'widget': TextInput(attrs={'size':'4'})},
    }


class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline, StepInline]
    list_display = ('name', 'meal_type', 'vegetarian', 'gluten_free', 'nut_free')
    list_filter = ['meal_type', 'vegetarian', 'gluten_free', 'nut_free']
    search_fields = ['name', 'description']


admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)
