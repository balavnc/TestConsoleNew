# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('appium', '0003_auto_20170316_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='appiumdevices',
            name='device_brand',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='appiumdevices',
            name='device_ip',
            field=models.GenericIPAddressField(default=b'0.0.0.0', validators=[django.core.validators.validate_ipv46_address]),
        ),
        migrations.AddField(
            model_name='appiumdevices',
            name='device_mac',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='appiumdevices',
            name='device_name',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
