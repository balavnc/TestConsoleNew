# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appium', '0007_auto_20170317_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appiumdevices',
            name='device_type',
            field=models.CharField(max_length=10, choices=[(b'Android', b'Android'), (b'IOS', b'IOS')]),
        ),
        migrations.AlterField(
            model_name='appiumos',
            name='os_type',
            field=models.CharField(max_length=10, choices=[(b'Android', b'Android'), (b'IOS', b'IOS')]),
        ),
    ]
