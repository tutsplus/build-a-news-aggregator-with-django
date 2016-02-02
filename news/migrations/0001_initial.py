# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('description', models.TextField()),
                ('publication_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='feed',
            field=models.ForeignKey(to='news.Feed'),
        ),
    ]
