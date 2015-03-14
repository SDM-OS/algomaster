# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_auto_20150314_0124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='slug',
        ),
    ]
