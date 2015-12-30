# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishcamps', '0005_auto_20151216_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='Age',
            field=models.IntegerField(default=0, max_length=2),
        ),
    ]
