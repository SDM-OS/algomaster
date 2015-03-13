# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20150313_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='algorithm',
        ),
        migrations.AddField(
            model_name='content',
            name='resource',
            field=models.ManyToManyField(to='content.Resource'),
            preserve_default=True,
        ),
    ]
