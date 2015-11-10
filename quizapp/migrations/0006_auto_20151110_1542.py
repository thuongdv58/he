# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0005_auto_20151110_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='picker_answer',
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 10, 15, 42, 15, 639000), verbose_name=b'date published'),
        ),
    ]
