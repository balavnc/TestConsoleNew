# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appium', '0011_auto_20170322_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='appiumdevices',
            name='device_serial',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='appiumdevices',
            name='device_model',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
