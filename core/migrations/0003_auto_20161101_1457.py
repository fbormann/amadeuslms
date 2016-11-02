# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-01 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20161024_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='component',
            field=models.TextField(default='', verbose_name='Component (Module / App)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='log',
            name='context',
            field=models.TextField(blank=True, verbose_name='Context'),
        ),
    ]
