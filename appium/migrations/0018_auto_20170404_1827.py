# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import macaddress.fields


class Migration(migrations.Migration):

    dependencies = [
        ('appium', '0017_auto_20170404_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appiumdevices',
            name='device_mac',
            field=macaddress.fields.MACAddressField(max_length=17, null=True, integer=False, blank=True),
        ),
    ]
