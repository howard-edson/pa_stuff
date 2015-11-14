# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('meal_type', models.CharField(max_length=50, choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Dessert', 'Dessert'), ('Appetizer', 'Appetizer'), ('Snack', 'Snack')])),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('quantity', models.CharField(max_length=50)),
                ('unit_of_measure', models.CharField(max_length=50, choices=[('oz', 'oz'), ('c', 'c'), ('tsp', 'tsp'), ('TBSP', 'TBSP'), ('pinch', 'pinch'), ('lb', 'lb')])),
                ('vegetarian', models.BooleanField(default=False)),
                ('gluten_free', models.BooleanField(default=False)),
                ('nut_free', models.BooleanField(default=False)),
                ('ingredient', models.ForeignKey(to='recipes.Ingredient')),
                ('recipe', models.ForeignKey(to='recipes.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeStep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('recipe', models.ForeignKey(to='recipes.Recipe')),
            ],
        ),
    ]
