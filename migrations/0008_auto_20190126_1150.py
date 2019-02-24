# Generated by Django 2.1.5 on 2019-01-26 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_auto_20190126_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formconfig',
            name='recaptcha_secret',
        ),
        migrations.RemoveField(
            model_name='formconfig',
            name='recaptcha_sitekey',
        ),
        migrations.AddField(
            model_name='formconfig',
            name='recaptcha',
            field=models.BooleanField(default=False, verbose_name='Use reCAPTCHA'),
        ),
    ]
