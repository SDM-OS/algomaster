# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20150313_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='algo_type',
            field=models.IntegerField(max_length=20, choices=[(1, b'Sorting'), (2, b'Search'), (3, b'Data Structure'), (4, b'Heaps'), (5, b'Graphs')]),
            preserve_default=True,
        ),
    ]
