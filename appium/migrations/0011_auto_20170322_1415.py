# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appium', '0010_auto_20170321_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnvironmentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, blank=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='appiumtestcase',
            options={'ordering': ['device_type']},
        ),
        migrations.AddField(
            model_name='appiumdevices',
            name='device_env',
            field=models.ForeignKey(to='appium.EnvironmentType', null=True),
        ),
    ]
