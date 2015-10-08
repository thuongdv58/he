# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0002_auto_20151007_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='isAnswer',
            field=models.BooleanField(default=False),
        ),
    ]
