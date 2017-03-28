from django.test import TestCase

# Create your tests here.


import win32com.client


wmi = win32com.client.GetObject(r"winmgmts:")
dev=[]
for usb in wmi.InstancesOf(r"Win32_USBHub"):
    dev.append(usb.DeviceID)

print dev
