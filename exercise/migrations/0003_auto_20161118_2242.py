# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-19 01:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0002_auto_20161117_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='file_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exercise_type', to='core.MimeType', verbose_name='Type file'),
        ),
    ]