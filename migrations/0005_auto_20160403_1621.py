# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-03 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20160403_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formfield',
            name='choices',
            field=models.TextField(blank=True, null=True, verbose_name='Choices'),
        ),
    ]
