# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Age', models.IntegerField(default=0)),
                ('NRIC', models.TextField(max_length=10)),
                ('Organisation', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WishCamp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('hobby_involved', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('number_of_people', models.IntegerField(default=1)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('estimated_date', models.DateField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='camp',
            field=models.ForeignKey(to='wishcamps.WishCamp'),
        ),
    ]
