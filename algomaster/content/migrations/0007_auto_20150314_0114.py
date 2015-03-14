# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_content_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='resource',
            field=models.ManyToManyField(to='content.Resource', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='content',
            name='slug',
            field=models.SlugField(null=True),
            preserve_default=True,
        ),
    ]
