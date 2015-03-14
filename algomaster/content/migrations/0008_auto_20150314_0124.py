# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_auto_20150314_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='resource_type',
            field=models.IntegerField(choices=[(1, b'video'), (2, b'tutorial'), (3, b'code')]),
            preserve_default=True,
        ),
    ]
