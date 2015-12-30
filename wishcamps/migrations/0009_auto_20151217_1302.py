# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('wishcamps', '0008_auto_20151217_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='Age',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(2)]),
        ),
    ]
