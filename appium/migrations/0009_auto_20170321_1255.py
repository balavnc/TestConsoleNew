# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import macaddress.fields


class Migration(migrations.Migration):

    dependencies = [
        ('appium', '0008_auto_20170317_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name='appiumos',
            options={'ordering': ['os_type']},
        ),
        migrations.RenameField(
            model_name='appiumdevices',
            old_name='device_brand',
            new_name='device_model',
        ),
        migrations.RemoveField(
            model_name='appiumdevices',
            name='device_ip',
        ),
        migrations.AddField(
            model_name='appiumdevices',
            name='device_version',
            field=models.ForeignKey(to='appium.AppiumOS', null=True),
        ),
        migrations.AlterField(
            model_name='appiumdevices',
            name='device_mac',
            field=macaddress.fields.MACAddressField(max_length=17, null=True, integer=False),
        ),
    ]
