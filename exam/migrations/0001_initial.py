# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-17 03:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=300, verbose_name='Answer')),
                ('order', models.PositiveSmallIntegerField(verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Answer',
                'ordering': ('order',),
                'verbose_name_plural': 'Answers',
            },
        ),
        migrations.CreateModel(
            name='AnswersStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, verbose_name='Answered')),
                ('answered_in', models.DateTimeField(auto_now=True, verbose_name='Answered Date')),
                ('answer', models.ManyToManyField(related_name='student_answer', to='exam.Answer', verbose_name='Answers Students')),
            ],
            options={
                'verbose_name': 'Answer Stundent',
                'verbose_name_plural': 'Answers Student',
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('activity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='courses.Activity')),
                ('begin_date', models.DateField(blank=True, verbose_name='Begin of Course Date')),
                ('exibe', models.BooleanField(default=False, verbose_name='Exibe?')),
            ],
            options={
                'verbose_name': 'Exam',
                'verbose_name_plural': 'Exams',
            },
            bases=('courses.activity',),
        ),
        migrations.AddField(
            model_name='answersstudent',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_exam', to='exam.Exam', verbose_name='Exam'),
        ),
    ]
