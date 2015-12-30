# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('campR', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personalinfo',
            old_name='Age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='personalinfo',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='personalinfo',
            old_name='Organisation',
            new_name='organisation',
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='registered_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
