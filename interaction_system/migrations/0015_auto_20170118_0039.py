# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 19:09
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interaction_system', '0014_auto_20170118_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_year',
            field=models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1600), django.core.validators.MaxValueValidator(2100)]),
        ),
        migrations.AlterField(
            model_name='location',
            name='continent',
            field=models.CharField(choices=[('Africa', 'Africa'), ('Antarctica', 'Antarctica'), ('Asia', 'Asia'), ('Australia', 'Australia'), ('Europe', 'Europe'), ('North America', 'North America'), ('South America', 'South America')], max_length=15),
        ),
    ]
