# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campR', '0002_auto_20151217_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='NRIC',
            field=models.CharField(unique=True, max_length=10, error_messages={b'unique': b'This NRIC has already been registerted for the camp!'}),
        ),
    ]
