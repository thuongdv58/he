# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0006_auto_20151110_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='picker_answer',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 10, 15, 42, 48, 291000), verbose_name=b'date published'),
        ),
    ]
