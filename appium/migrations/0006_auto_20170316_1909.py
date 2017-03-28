# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appium', '0005_appiumos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appiumos',
            old_name='device_type',
            new_name='os_type',
        ),
        migrations.RenameField(
            model_name='appiumos',
            old_name='device_version',
            new_name='os_version',
        ),
    ]
