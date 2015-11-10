# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0007_auto_20151110_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.ForeignKey(to='quizapp.answer', blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='multi_select_answer',
            field=models.ManyToManyField(to='quizapp.multi_answer', blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 10, 16, 2, 58, 983000), verbose_name=b'date published'),
        ),
    ]
