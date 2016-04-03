# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-03 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_auto_20160403_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='subject',
        ),
        migrations.AlterModelOptions(
            name='formfield',
            options={'ordering': ['order'], 'verbose_name': 'Field', 'verbose_name_plural': 'Fields'},
        ),
        migrations.AddField(
            model_name='formfield',
            name='order',
            field=models.IntegerField(default=500, verbose_name='Sort ordering'),
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
