# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appium', '0013_auto_20170328_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appiumdevices',
            name='device_model',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='appiumdevices',
            name='device_serial',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
