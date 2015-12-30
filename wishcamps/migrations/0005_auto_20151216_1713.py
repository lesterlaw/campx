# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishcamps', '0004_auto_20151216_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='NRIC',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterUniqueTogether(
            name='personalinfo',
            unique_together=set([('NRIC', 'camp')]),
        ),
    ]
