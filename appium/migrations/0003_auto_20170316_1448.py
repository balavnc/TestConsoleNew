# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appium', '0002_auto_20170316_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appiumdevices',
            name='device_type',
            field=models.CharField(max_length=1, choices=[(1, b'Android'), (2, b'IOS')]),
        ),
    ]
