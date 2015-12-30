# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=100)),
                ('Age', models.CharField(max_length=2, validators=[django.core.validators.RegexValidator(b'^\\d{1,10}$')])),
                ('NRIC', models.CharField(unique=True, max_length=10)),
                ('Organisation', models.CharField(max_length=100)),
            ],
        ),
    ]
