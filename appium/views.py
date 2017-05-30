from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from django.template import RequestContext
from django.contrib.auth.decorators import login_required
import json
import jenkins
import os, time
from datetime import datetime
import socket

from models import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Logger
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'runtime/logs/appium.log')
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

# creating file handlers
file_handler = RotatingFileHandler(filename, mode='a', maxBytes=1*1024*1024, 
                                 backupCount=3, encoding=None, delay=0)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# creating console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

logger.addHandler(logging.NullHandler())

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Jenkins 
hostname = socket.gethostname()
localhost = socket.gethostbyname(hostname)

jenkins_username='jenkins'
jenkins_password='jenkins123'

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


# Create your views here.
       
@login_required
def appium_home(request):
    assert isinstance(request, HttpRequest)
    logger.info("Welcome to Appium Page")
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
    logger.debug("Devices and Test Suite Cases selected :: " + str(post_data))
    #parsing data
    android_devices = post_data['devices_android']
    ios_devices = post_data['devices_ios']
    android_suites = post_data['suites_android']
    ios_suites = post_data['suites_ios']
    android_suite_cases =  { suite["name"]:suite["cases_android"] for suite in android_suites}
    ios_suite_cases = { suite["name"]:suite["cases_ios"] for suite in ios_suites}
    tester = request.user.username
    
    logger.info("Requester Username : "+ str(tester))
    logger.info(" Devices Selected : Android - " + str(android_devices) + " IOS - " + str(ios_devices))
    logger.info(" TestSuites Selected : Android - " + str(android_suites) + " IOS - " + str(ios_suites))
    logger.debug(" TestSuiteCases Selected : Android - " + str(android_suite_cases) + " IOS - " + str(ios_suite_cases))
    
    for device in android_devices:
        count=0
        for suite, cases in android_suite_cases.items():
            if cases:
                count +=1
                cases=' '.join(cases)
                appium_create_jobs(device,suite,cases)
                logger.info("Creating Android Job : >> " + str(count) )
                
    for device in ios_devices:
        count=0
        for suite, cases in ios_suite_cases.items():
            if cases:
                count +=1
                cases=' '.join(cases)
                appium_create_jobs(device,suite,cases)
                logger.info("Creating IOS Job : >> " + str(count) )
      
    return HttpResponse(post_data, content_type='application/json') 

def appium_create_jobs(device, suite, cases):
    
    logger.debug("Connecting to Jenkins server...")
    server = jenkins.Jenkins('http://'+localhost+':8080',jenkins_username,jenkins_password)
    new_folder_config = '<com.cloudbees.hudson.plugins.folder.Folder plugin="cloudbees-folder@6.0.3"><actions/><description/><displayName>Appium Jobs</displayName><properties/><views><hudson.model.AllView><owner class="com.cloudbees.hudson.plugins.folder.Folder" reference="../../.."/><name>All</name><filterExecutors>false</filterExecutors><filterQueue>false</filterQueue><properties class="hudson.model.View$PropertyList"/></hudson.model.AllView></views><viewsTabBar class="hudson.views.DefaultViewsTabBar"/><healthMetrics><com.cloudbees.hudson.plugins.folder.health.WorstChildHealthMetric/></healthMetrics><icon class="com.cloudbees.hudson.plugins.folder.icons.StockFolderIcon"/></com.cloudbees.hudson.plugins.folder.Folder>'

    if not server.job_exists('appium'):
        server.create_job('appium', new_folder_config)
        logger.debug("Creating Jenkins Folder - Appium")
    
    appium_server = jenkins.Jenkins('http://'+localhost+':8080/job/appium/',jenkins_username,jenkins_password)
    new_job_config="<?xml version='1.0' encoding='UTF-8'?><project><actions/><description>DESCRIPTION</description><keepDependencies>true</keepDependencies><properties/><scm class='hudson.scm.NullSCM'/><canRoam>true</canRoam><disabled>false</disabled><blockBuildWhenDownstreamBuilding>true</blockBuildWhenDownstreamBuilding><blockBuildWhenUpstreamBuilding>true</blockBuildWhenUpstreamBuilding><triggers/><concurrentBuild>true</concurrentBuild><builders><hudson.tasks.BatchFile><command>COMMAND</command></hudson.tasks.BatchFile></builders><publishers/><buildWrappers/></project>"
    
    job_name=device +'-'+suite
    job_desc =suite +'-'+cases
    command ='ping 127.0.0.1 -n 100 > nul'
    logger.debug(" Job Name : " + job_name + " Job Description : " + job_desc + " Command : " + command)
    
    if not appium_server.job_exists(job_name):
        appium_server.create_job(job_name, new_job_config.replace('DESCRIPTION',job_desc).replace('COMMAND', command))
        logger.info("Created Job successfully >> " + job_name)
    else:
        appium_server.reconfig_job(job_name, new_job_config.replace('DESCRIPTION',job_desc).replace('COMMAND', command))
        logger.info("Reconfigured Job successfully >> " + job_name)
        
    time.sleep(5)
    logger.info("Waiting for 5 seconds...")
        
    if appium_server.job_exists(job_name):
        appium_server.build_job(job_name)
        logger.info("Building job >> " + job_name)
       

    
def appium_job_status(request):
    
    job_status_list=[]
    
    logger.debug("Connecting to Jenkins server...")
    appium_server = jenkins.Jenkins('http://'+localhost+':8080/job/appium/',jenkins_username,jenkins_password)
    info = appium_server.get_info()
    jobs = info['jobs']
    
    count=0
    logger.info("Fetching Appium Jobs and their statuses from Jenkins :::")
    
    for job in jobs:
            count +=1
            job_name=job['name']
            job_info = appium_server.get_job_info(job_name)
            logger.debug("Jenkins Job Info >> " + str(job_info))
            JobName= job_info['name']
            Build='...'
            Result = "NOT BUILT"
            StartTime = '------'
            EndTime = '------'
            Duration = '...'
            
            if job_info['lastBuild']:
                Build= job_info['lastBuild']['number']
                build_info = appium_server.get_build_info(job_name, Build)
            
                if build_info['building']:
                    Result = "IN PROGRESS"
                    StartTime = time.strftime('%m/%d/%Y %H:%M:%S',time.gmtime(((int(build_info['timestamp'])) - 23400000) / 1000))
                    
                else:
                    Result = build_info['result']
                    StartTime = time.strftime('%m/%d/%Y %H:%M:%S', time.gmtime(((int(build_info['timestamp'])) - 23400000) / 1000))
                    EndTime = time.strftime('%m/%d/%Y %H:%M:%S', time.gmtime(((int(build_info['timestamp']) + int(build_info['duration']) - 23400000) / 1000)))
                    Duration= build_info['duration']
                    
            job_dict={}
            job_dict['Devices']=JobName.split('-',1)[0]
            job_dict['SuiteName']=JobName.split('-',1)[1]
            job_dict['JobName']=JobName
            job_dict['Build']=Build
            job_dict['Result']=Result
            job_dict['StartTime']=StartTime
            job_dict['EndTime']=EndTime
            job_dict['Duration']=Duration
            job_dict['Tester']=request.user.username
            job_status_list.append(job_dict)
            
            logger.info( str(count) + " >> " + str(job_dict))
            
    data = json.dumps(job_status_list)
    return HttpResponse(data, content_type='application/json')
    
 
def consolelink(request):
    assert isinstance(request, HttpRequest)
    job = request.GET["job"]
    build = int(request.GET["build"])
    logger.debug("Connecting to Jenkins server...")
    appium_server = jenkins.Jenkins('http://'+localhost+':8080/job/appium/',jenkins_username,jenkins_password)
    output = appium_server.get_build_console_output(job, build)
    logger.info("Jenkins Job Console Output :: " + output)
    return HttpResponse(output)


def stopJob(request):
    assert isinstance(request, HttpRequest)
    job = request.GET["job"]
    build = int(request.GET["build"])
    PRINT_JOB_INFO = str("Job:" + job + "  Build No: " + str(build))
    logger.info("Job to Stop ==>> " + PRINT_JOB_INFO )
    
    logger.debug("Connecting to Jenkins server...")
    server = jenkins.Jenkins('http://'+localhost+':8080',jenkins_username,jenkins_password)
    appium_server = jenkins.Jenkins('http://'+localhost+':8080/job/appium/',jenkins_username,jenkins_password)
    
    job_info = appium_server.get_job_info(job)
    
    if job_info['queueItem']:
        queue_id=job_info['queueItem']['id']
        PRINT_QUEUE_INFO = "Job: " + job + "  Build "+ str(build+1) +" with Queue Id: " + queue_id
        server.cancel_queue(queue_id)
        logger.info( "CANCELLED QUEUE ==>> " + PRINT_QUEUE_INFO )
        
    appium_server.stop_build(job, build)
    logger.info( "STOPPED BUILD: ==>> "+ PRINT_JOB_INFO )
        
    return HttpResponse(json.dumps({"done" : True }), content_type='application/json')


def StopMultipleJobs(request):
    assert isinstance(request, HttpRequest)

    builds_list = request.POST.getlist('build')
    logger.info( "Jobs List to Stop: ==>> ",  builds_list)
    
    logger.debug("Connecting to Jenkins server...")
    appium_server = jenkins.Jenkins('http://'+localhost+':8080/job/appium/',jenkins_username,jenkins_password)
        
#     if builds_list:
#         for build_info in builds_list:
#             info = str(build_info)
#             job = info.split(",")[0]
#             build = int(info.split(",")[1])
#             appium_server.stop_build(job, build)
            

    return HttpResponseRedirect("/appium")

    
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
    logger.debug("Devices serial no list in DB :: " + str(device_serial_list))
    # CoInitialize() to run wmi as a child to avoid com_error
    pythoncom.CoInitialize()
    wmi = win32com.client.GetObject("winmgmts:")
    active_devices_list=[]
    
    for device_serial_id in device_serial_list:
        for usb in wmi.InstancesOf("Win32_USBHub"):
            if str(device_serial_id).upper() in usb.DeviceID.upper():
                active_devices_list.append(device_serial_id)
                
    pythoncom.CoUninitialize()
    #logger.info("Connected devices Serial Nos list :: " + active_devices_list)
    return active_devices_list

def appium_android_devices_list(request):
    assert isinstance(request, HttpRequest)
    
    active_devices_list= devices_is_connected()
    logger.info("Connected Android devices Serial Nos list :: " + str(active_devices_list))
    
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
    logger.info("Connected IOS devices Serial Nos list :: " + str(active_devices_list))
    
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

