# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20151107_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipestep',
            name='description',
            field=models.TextField(),
        ),
    ]
