from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(AppiumTestCase)
admin.site.register(AppiumTestSuite)
admin.site.register(AppiumDevices)
admin.site.register(AppiumOS)
admin.site.register(DeviceType)
admin.site.register(EnvironmentType)