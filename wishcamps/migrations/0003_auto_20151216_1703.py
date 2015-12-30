# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishcamps', '0002_auto_20151216_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishcamp',
            name='number_of_people',
            field=models.IntegerField(default=0),
        ),
    ]
