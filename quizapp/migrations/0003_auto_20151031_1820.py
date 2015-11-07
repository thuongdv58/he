# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0002_auto_20151030_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='rate',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 31, 18, 20, 23, 766000), verbose_name=b'date published'),
        ),
    ]
