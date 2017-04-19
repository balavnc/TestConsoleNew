from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse_lazy, reverse

from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from datetime import datetime, date, timedelta
import json
import jenkins
import os, time

from models import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

import socket

hostname = socket.gethostname()
localhost = socket.gethostbyname(hostname)
# Create your views here.

        
@login_required
def appium_home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "appium/appium.html",
        
        RequestContext(request, {
            "title":"Appium",
            "message":"Stuff about Appium goes here.",
             "year":datetime.now().year,
        })
)
  
def appium_run_job(request):
    post_data = json.loads(request.body)
   
    #parsing data
    android_devices = post_data['devices_android']
    ios_devices = post_data['devices_ios']
    android_suites =  [ suite["name"] for suite in post_data['suites_android']]
    ios_suites = [ suite["name"] for suite in post_data['suites_ios']]
    android_suites_cases = []
    [ android_suites_cases.extend(i) for i in [suite["cases_android"] for suite in post_data['suites_android']]]
    android_test_cases = list(set(android_suites_cases))
    ios_suites_cases = []
    [ ios_suites_cases.extend(i) for i in [suite["cases_ios"] for suite in post_data['suites_ios']]]
    ios_test_cases = list(set(ios_suites_cases))
    tester = request.user.username
    
    print android_test_cases
    print ios_test_cases
    
    appium_create_jobs()
       
    return HttpResponse(post_data, content_type='application/json') 

def appium_create_jobs():
    
    server = jenkins.Jenkins('http://'+localhost+':8080')
    new_folder_config = '<com.cloudbees.hudson.plugins.folder.Folder plugin="cloudbees-folder@6.0.3"><actions/><description/><displayName>appium</displayName><properties/><views><hudson.model.AllView><owner class="com.cloudbees.hudson.plugins.folder.Folder" reference="../../.."/><name>All</name><filterExecutors>false</filterExecutors><filterQueue>false</filterQueue><properties class="hudson.model.View$PropertyList"/></hudson.model.AllView></views><viewsTabBar class="hudson.views.DefaultViewsTabBar"/><healthMetrics><com.cloudbees.hudson.plugins.folder.health.WorstChildHealthMetric/></healthMetrics><icon class="com.cloudbees.hudson.plugins.folder.icons.StockFolderIcon"/></com.cloudbees.hudson.plugins.folder.Folder>'

    if not server.job_exists('appium'):
        server.create_job('appium', new_folder_config)
    
    appium_server = jenkins.Jenkins('http://'+localhost+':8080/job/appium/')
    new_job_config="<?xml version='1.0' encoding='UTF-8'?><project><actions/><description>Appium Job</description><keepDependencies>true</keepDependencies><properties/><scm class='hudson.scm.NullSCM'/><canRoam>true</canRoam><disabled>false</disabled><blockBuildWhenDownstreamBuilding>true</blockBuildWhenDownstreamBuilding><blockBuildWhenUpstreamBuilding>true</blockBuildWhenUpstreamBuilding><triggers/><concurrentBuild>true</concurrentBuild><builders><hudson.tasks.BatchFile><command>COMMAND</command></hudson.tasks.BatchFile></builders><publishers/><buildWrappers/></project>"
    command ='echo %date%'
    job_name='job3'
    
    appium_server.create_job(job_name, new_job_config.replace('COMMAND', command))
    time.sleep(5)
    
    if appium_server.job_exists(job_name):
        appium_server.build_job(job_name)
       

 
    
def appium_job_status(request):
    
    job_status_list=[]
    
    appium_server = jenkins.Jenkins('http://'+localhost+':8080/job/appium/')
    info = appium_server.get_info()
    jobs = info['jobs']
    
    for job in jobs:
            job_name=job['name']
            job_info = appium_server.get_job_info(job_name)
            JobName= job_info['name']
            Build='...'
            Result = "NOT BUILT"
            StartTime = '------'
            EndTime = '------'
            Duration = '...'
            
            if job_info['lastCompletedBuild']:
                Build= job_info['lastCompletedBuild']['number']
                build_info = appium_server.get_build_info(job_name, Build) 
            
                if str(build_info['result']) == 'None':
                    Result = "IN PROGRESS"
                    StartTime = time.strftime('%m/%d/%Y %H:%M:%S',time.gmtime(((int(build_info['timestamp'])) - 18000000) / 1000))
                    
        
                else:
                    Result = build_info['result']
                    StartTime = time.strftime('%m/%d/%Y %H:%M:%S', time.gmtime(((int(build_info['timestamp'])) - 18000000) / 1000))
                    EndTime = time.strftime('%m/%d/%Y %H:%M:%S', time.gmtime(((int(build_info['timestamp']) + int(build_info['duration']) - 18000000) / 1000)))
                    Duration= build_info['duration']
                    
            job_dict={}
            job_dict['Devices']='Devices -'+JobName
            job_dict['SuiteName']='Suite -'+JobName
            job_dict['JobName']=JobName
            job_dict['Build']=Build
            job_dict['Result']=Result
            job_dict['StartTime']=StartTime
            job_dict['EndTime']=EndTime
            job_dict['Duration']=Duration
            job_dict['Tester']=request.user.username
            job_status_list.append(job_dict)
            
    
    data = json.dumps(job_status_list)
    return HttpResponse(data, content_type='application/json')
    
    
# Appium Test Suite Cases as Json
def appium_android_test_suite_cases(request):
    assert isinstance(request, HttpRequest)
    
    resp = {}
    test_suites = AppiumTestSuite.objects.filter(test_suite_type__name='Android')
    for suite in test_suites:
        test_cases_list = [ test_case.test_case_id for test_case in suite.test_cases_list.all() ]
        resp[suite.test_suite_name] = test_cases_list

    data = json.dumps(resp)            
    return HttpResponse(data, content_type='application/json')

def appium_ios_test_suite_cases(request):
    assert isinstance(request, HttpRequest)
    
    resp = {}
    test_suites = AppiumTestSuite.objects.filter(test_suite_type__name='IOS')
    for suite in test_suites:
        test_cases_list = [ test_case.test_case_id for test_case in suite.test_cases_list.all() ]
        resp[suite.test_suite_name] = test_cases_list

    data = json.dumps(resp)            
    return HttpResponse(data, content_type='application/json')


# Appium Devices List as Json
import win32com.client
import pythoncom

def devices_is_connected():
    device_serial_list = [x.device_serial for x in AppiumDevices.objects.all()]
    # CoInitialize() to run wmi as a child to avoid com_error
    pythoncom.CoInitialize()
    wmi = win32com.client.GetObject("winmgmts:")
     
    active_devices_list=[]
    for device_serial_id in device_serial_list:
        for usb in wmi.InstancesOf("Win32_USBHub"):
            if str(device_serial_id).upper() in usb.DeviceID.upper():
                active_devices_list.append(device_serial_id)
                
    pythoncom.CoUninitialize()
    return active_devices_list

def appium_android_devices_list(request):
    assert isinstance(request, HttpRequest)
    
    active_devices_list= devices_is_connected()
    resp = []
    devices_list = AppiumDevices.objects.filter(device_type__name='Android')
    for device in devices_list:
        d={}
        d["DevicesLabel"]=str(device.device_name +' '+device.device_model)
        d["DevicesStatus"]= 1 if str(device.device_serial) in active_devices_list else 0
        d["Version"]=str(device.device_version.os_version)
        d["SerialNo"]=str(device.device_serial)
        d["Env"]=str(device.device_env.name)
        resp.append(d)
     
    data = json.dumps(resp)            
    return HttpResponse(data, content_type='application/json')

def appium_ios_devices_list(request):
    assert isinstance(request, HttpRequest)
    
    active_devices_list= devices_is_connected()
    resp = []
    devices_list = AppiumDevices.objects.filter(device_type__name='IOS')
    for device in devices_list:
        d={}
        d["DevicesLabel"]=str(device.device_name +' '+device.device_model)
        d["DevicesStatus"]= 1 if str(device.device_serial) in active_devices_list else 0
        d["Version"]=str(device.device_version.os_version)
        d["SerialNo"]=str(device.device_serial)
        d["Env"]=str(device.device_env.name)
        resp.append(d)
        
    data = json.dumps(resp)            

#     script_dir = os.path.dirname(os.path.abspath(__file__))
#     fname = os.path.join(script_dir, "iosStatus.json")
#     with open(fname, 'w') as f:
#         f.write(data)
        
    return HttpResponse(data, content_type='application/json')

def appium_android_test_cases(request):
    assert isinstance(request, HttpRequest)
    resp = []
    test_cases = AppiumTestCase.objects.filter(test_case_type__name='Android')
    
    for test_case in test_cases:
        resp.append(test_case.test_case_id)
    
    print resp  
    data = json.dumps(resp)
    return HttpResponse(data, content_type='application/json')
    
def appium_ios_test_cases(request):
    assert isinstance(request, HttpRequest)
    resp = []
    test_cases = AppiumTestCase.objects.filter(test_case_type__name='IOS')
    
    for test_case in test_cases:
        resp.append(test_case.test_case_id)
        
    data = json.dumps(resp)
    return HttpResponse(data, content_type='application/json')
    


# Appium Device Configuration
class AppiumDeviceList(ListView):
    model = AppiumDevices
    context_object_name = 'appium_devices'

class AppiumDeviceCreate(CreateView):
    model = AppiumDevices
    fields = '__all__'

class AppiumDeviceUpdate(UpdateView):
    model = AppiumDevices
    fields = '__all__'
   
def AppiumDeviceDelete(request) :
    assert isinstance(request, HttpRequest)
    AppiumDevices.objects.filter(id__in=request.POST.getlist('device')).delete()
    return HttpResponseRedirect(reverse("appium_device_list"))

# Appium Test Suite Configuration
class AppiumTestSuiteList(ListView):
    model = AppiumTestSuite
    context_object_name = 'appium_test_suites'
    
class AppiumTestSuiteCreate(CreateView):
    model = AppiumTestSuite
    fields = '__all__'

class AppiumTestSuiteUpdate(UpdateView):
    model = AppiumTestSuite
    fields = '__all__'

def AppiumTestSuiteDelete(request) :
    assert isinstance(request, HttpRequest)
    AppiumTestSuite.objects.filter(id__in=request.POST.getlist('suite')).delete()
    return HttpResponseRedirect(reverse("appium_test_suite_list"))

# Appium Test Case Configuration
class AppiumTestCaseList(ListView):
    model = AppiumTestCase
    context_object_name = 'appium_test_cases'

class AppiumTestCaseCreate(CreateView):
    model = AppiumTestCase
    fields = '__all__'

class AppiumTestCaseUpdate(UpdateView):
    model = AppiumTestCase
    fields = '__all__'
    
def AppiumTestCaseDelete(request) :
    assert isinstance(request, HttpRequest)
    AppiumTestCase.objects.filter(id__in=request.POST.getlist('test_case')).delete()
    return HttpResponseRedirect(reverse("appium_test_case_list"))


# Appium OS & Version Configuration
class AppiumOSList(ListView):
    model = AppiumOS
    context_object_name = 'appium_os_versions'

class AppiumOSCreate(CreateView):
    model = AppiumOS
    fields = '__all__'

class AppiumOSUpdate(UpdateView):
    model = AppiumOS
    fields = '__all__'
    
def AppiumOSDelete(request):
    assert isinstance(request, HttpRequest)
    AppiumOS.objects.filter(id__in=request.POST.getlist('os_version')).delete()
    return HttpResponseRedirect(reverse("appium_os_list"))

