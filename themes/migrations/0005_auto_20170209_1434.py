# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-09 17:34
from __future__ import unicode_literals

from django.db import migrations, models
import themes.models


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0004_themes_favicon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='themes',
            name='favicon',
            field=models.ImageField(blank=True, null=True, upload_to='themes/', validators=[themes.models.validate_img_extension], verbose_name='Favicon'),
        ),
        migrations.AlterField(
            model_name='themes',
            name='large_logo',
            field=models.ImageField(blank=True, null=True, upload_to='themes/', validators=[themes.models.validate_img_extension], verbose_name='Large Logo'),
        ),
        migrations.AlterField(
            model_name='themes',
            name='small_logo',
            field=models.ImageField(blank=True, null=True, upload_to='themes/', validators=[themes.models.validate_img_extension], verbose_name='Small Logo'),
        ),
    ]