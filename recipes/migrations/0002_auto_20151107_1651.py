# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipeingredient',
            name='gluten_free',
        ),
        migrations.RemoveField(
            model_name='recipeingredient',
            name='nut_free',
        ),
        migrations.RemoveField(
            model_name='recipeingredient',
            name='vegetarian',
        ),
        migrations.AddField(
            model_name='recipe',
            name='gluten_free',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recipe',
            name='nut_free',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recipe',
            name='vegetarian',
            field=models.BooleanField(default=False),
        ),
    ]
