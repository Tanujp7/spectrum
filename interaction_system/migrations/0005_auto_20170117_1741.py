# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interaction_system', '0004_auto_20170117_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='location',
            name='state',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
