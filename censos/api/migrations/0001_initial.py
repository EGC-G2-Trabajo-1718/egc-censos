# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 17:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Censo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_votacion', models.IntegerField()),
                ('id_grupo', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_ini', models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 4, 17, 34, 6, 411239))),
                ('fecha_fin', models.DateTimeField(blank=True)),
            ],
            options={
                'db_table': 'censo',
                'managed': True,
            },
        ),
    ]
