# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20151107_1706'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipestep',
            options={'ordering': ['sequence']},
        ),
        migrations.AddField(
            model_name='recipestep',
            name='sequence',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipestep',
            name='description',
            field=models.CharField(max_length=254),
        ),
    ]
