# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-03 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_officefeature'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formconfig',
            options={'ordering': ['-created_at'], 'verbose_name': 'Form config', 'verbose_name_plural': 'Forms configs'},
        ),
        migrations.AddField(
            model_name='formconfig',
            name='success_message',
            field=models.TextField(blank=True, verbose_name='Success message'),
        ),
    ]
