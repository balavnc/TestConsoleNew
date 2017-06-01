from django.db import models
from django.core.urlresolvers import reverse_lazy
from macaddress.fields import MACAddressField

# Create your models here.
class DeviceType(models.Model):
    name = models.CharField(max_length=255,unique=True, blank=True)
     
    def __unicode__(self):
        return self.name
    
class EnvironmentType(models.Model):
    name = models.CharField(max_length=255,unique=True, blank=True)
     
    def __unicode__(self):
        return self.name
    
class AppiumTestCase(models.Model):
    test_case_type = models.ForeignKey(DeviceType, null=True)
    test_case_id = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse_lazy('appium_test_case_list')
    
    def __unicode__(self):
        return self.test_case_id
    
    class Meta:
        ordering = ['test_case_type']
    

class AppiumTestSuite(models.Model):
    test_suite_type = models.ForeignKey(DeviceType, null=True)
    test_suite_name = models.CharField(max_length=255)
    test_cases_list = models.ManyToManyField(AppiumTestCase, related_name="testsuites")

    def get_absolute_url(self):
        return reverse_lazy('appium_test_suite_list')

    def __unicode__(self):
        return self.test_suite_name
 

class AppiumOS(models.Model):
    os_type = models.ForeignKey(DeviceType, null=True)
    os_version = models.CharField(max_length=255, unique=True)
    
    def get_absolute_url(self):
        return reverse_lazy('appium_os_list')

    def __unicode__(self):
        return self.os_version
    
    class Meta:
        ordering = ['os_type']

# To create version choices for Appium Devices
# version_list=[str(i.os_type +'-> '+ i.os_version) for i in AppiumOS.objects.all()]        
# VERSION_TUPLE = tuple(zip(version_list,version_list))

class AppiumDevices(models.Model):
    device_name = models.CharField(max_length=255, null=True)
    device_mac = MACAddressField(integer=False, null=True, blank=True)
    device_serial = models.CharField(max_length=255, unique=True)
    device_type = models.ForeignKey(DeviceType, null=True)
    device_version = models.ForeignKey(AppiumOS, null=True)
    device_env = models.ForeignKey(EnvironmentType, null=True)

    def get_absolute_url(self):
        return reverse_lazy('appium_device_list')

    def __unicode__(self):
        return self.device_name
 

 
