# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appium', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppiumDevices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device_name', models.CharField(max_length=100)),
                ('device_type', models.CharField(max_length=1, choices=[(b'choco', b'Chocolate'), (b'vani', b'Vanilla')])),
            ],
        ),
        migrations.AlterField(
            model_name='appiumtestcase',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
