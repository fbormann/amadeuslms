# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-10 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0005_auto_20170209_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='themes',
            name='css_style',
            field=models.CharField(choices=[('green', 'Green'), ('contrast', 'Contrast'), ('red', 'Red'), ('black', 'Black')], default='green', max_length=50, verbose_name='Css Style'),
        ),
    ]
