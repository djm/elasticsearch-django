# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-29 11:35
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elasticsearch_django', '0003_auto_20160926_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchquery',
            name='hits',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text=b'The list of meta info for each of the query matches returned.'),
        ),
        migrations.AlterField(
            model_name='searchquery',
            name='query',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text=b'The raw ElasticSearch DSL query.'),
        ),
    ]
