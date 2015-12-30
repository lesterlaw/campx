# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishcamps', '0003_auto_20151216_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='NRIC',
            field=models.CharField(unique=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='Organisation',
            field=models.CharField(max_length=100),
        ),
    ]
