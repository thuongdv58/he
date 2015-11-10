# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0003_auto_20151031_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='multi_answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='toggle_choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ob', models.CharField(max_length=30)),
                ('answer', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='fill_blank_answer',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='fill_two_blank1',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='fill_two_blank2',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='max',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='min',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='picker_answer',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='true_false_choice',
            field=models.BooleanField(default=True, choices=[(False, b'False'), (True, b'True')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 10, 8, 4, 49, 62000), verbose_name=b'date published'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='quizapp.Question'),
        ),
        migrations.AddField(
            model_name='question',
            name='multi_select_answer',
            field=models.ManyToManyField(to='quizapp.multi_answer'),
        ),
    ]
