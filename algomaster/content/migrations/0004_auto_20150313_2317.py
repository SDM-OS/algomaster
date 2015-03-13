# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20150313_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('link', models.URLField()),
                ('resource_type', models.IntegerField(choices=[(b'1', b'video'), (b'2', b'tutorial'), (b'3', b'code')])),
                ('algorithm', models.ManyToManyField(to='content.Content')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='content',
            name='algo_type',
            field=models.IntegerField(choices=[(1, b'Sorting'), (2, b'Search'), (3, b'Data Structure'), (4, b'Heaps'), (5, b'Graphs')]),
            preserve_default=True,
        ),
    ]
