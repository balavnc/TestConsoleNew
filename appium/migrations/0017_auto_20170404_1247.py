# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appium', '0016_auto_20170404_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appiumos',
            name='os_type',
            field=models.ForeignKey(to='appium.DeviceType', null=True),
        ),
    ]
