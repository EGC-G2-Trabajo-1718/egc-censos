# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-21 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20171204_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='censo',
            name='id_grupo',
        ),
        migrations.AddField(
            model_name='censo',
            name='rol',
            field=models.CharField(default='ASISTENTE', max_length=20),
        ),
    ]
