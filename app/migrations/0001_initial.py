# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-17 05:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailBackend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('host', models.URLField(verbose_name='E-mail Host')),
                ('port', models.CharField(blank=True, max_length=4, verbose_name='Email Port')),
                ('username', models.CharField(max_length=30, verbose_name='Email host username')),
                ('password', models.CharField(blank=True, max_length=30, verbose_name='Email host password')),
                ('safe_conection', models.IntegerField(choices=[(0, 'No'), (1, 'TLS, if available'), (2, 'TLS'), (3, 'SSL')], default=0, verbose_name='Use safe conection')),
                ('default_from_email', models.EmailField(max_length=254, verbose_name='Default from email')),
            ],
            options={
                'verbose_name_plural': 'Amadeus SMTP settings',
                'verbose_name': 'Amadeus SMTP setting',
            },
        ),
    ]
