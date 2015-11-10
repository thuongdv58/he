# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0004_auto_20151110_0804'),
    ]

    operations = [
        migrations.CreateModel(
            name='single_answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.IntegerField(default=0, max_length=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer1',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer2',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer3',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer4',
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 10, 15, 16, 8, 47000), verbose_name=b'date published'),
        ),
        migrations.AddField(
            model_name='question',
            name='single_answer',
            field=models.ForeignKey(default=1, to='quizapp.single_answer'),
        ),
    ]
