# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20150313_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='slug',
            field=models.SlugField(default='test'),
            preserve_default=False,
        ),
    ]
