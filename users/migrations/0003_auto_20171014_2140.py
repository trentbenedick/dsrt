# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-15 04:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20171014_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='SeriesDate',
            field=models.DateField(null=True),
        ),
    ]
