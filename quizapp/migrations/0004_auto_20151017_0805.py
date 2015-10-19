# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0003_auto_20151007_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(default=datetime.datetime(2015, 10, 17, 1, 5, 3, 964000, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
