# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-03 08:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20160403_1402'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=128, verbose_name='Label')),
                ('help_text', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Help text')),
                ('name', models.SlugField(max_length=100, verbose_name='Name')),
                ('required', models.BooleanField(default=True, verbose_name='Required')),
                ('choices', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Choices')),
                ('default', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Default')),
                ('placeholder', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Placeholder')),
                ('form_config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.FormConfig', verbose_name='Form Config')),
            ],
            options={
                'verbose_name': 'Field',
                'verbose_name_plural': 'Fields',
            },
        ),
    ]
