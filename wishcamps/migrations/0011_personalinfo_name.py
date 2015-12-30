# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishcamps', '0010_auto_20151217_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='name',
            field=models.CharField(default='name', max_length=100),
            preserve_default=False,
        ),
    ]
