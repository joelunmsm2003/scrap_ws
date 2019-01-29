# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-24 23:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180821_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historialglobo',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 8, 24, 18, 21, 27, 972576)),
        ),
        migrations.AlterField(
            model_name='historialglobo',
            name='fecha_fin',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 8, 24, 18, 21, 27, 972678)),
        ),
        migrations.AlterField(
            model_name='historialglobo',
            name='fecha_inicio',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 8, 24, 18, 21, 27, 972630)),
        ),
    ]
