# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appium', '0014_auto_20170328_1137'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appiumtestcase',
            options={'ordering': ['test_case_type']},
        ),
        migrations.AlterModelOptions(
            name='appiumtestsuite',
            options={'ordering': ['test_suite_name']},
        ),
        migrations.RenameField(
            model_name='appiumtestcase',
            old_name='device_type',
            new_name='test_case_type',
        ),
        migrations.RenameField(
            model_name='appiumtestsuite',
            old_name='device_type',
            new_name='test_suite_type',
        ),
    ]
