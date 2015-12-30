# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('wishcamps', '0009_auto_20151217_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='Age',
            field=models.CharField(max_length=2, validators=[django.core.validators.RegexValidator(b'^\\d{1,10}$')]),
        ),
    ]
