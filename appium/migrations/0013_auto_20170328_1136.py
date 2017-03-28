# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appium', '0012_auto_20170328_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appiumdevices',
            name='device_model',
            field=models.CharField(unique=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='appiumdevices',
            name='device_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
