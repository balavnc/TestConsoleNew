# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appium', '0004_auto_20170316_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppiumOS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device_version', models.CharField(unique=True, max_length=255)),
                ('device_type', models.CharField(max_length=1, choices=[(1, b'Android'), (2, b'IOS')])),
            ],
        ),
    ]
