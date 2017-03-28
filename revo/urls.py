from django.conf.urls import url
from . import views

# Conversion before production
# TODO: url = in lowercase and '-' separated
# TODO: name = in lowercase '_' separated
# function name = depending upon wether it is class or function

urlpatterns = [
	url(r'^$', views.revo_home, name='revo'),
    
    url(r'^revo_view/$', views.revo_view, name='revo_view'),
    url(r'^run', views.run_job, name='revo_run'),
    
    
# Console output	
    url(r'^console/$', views.consolelink, name='consolelink'),
# StopMultipleJobs's
    url(r"^StopMultipleJobs", views.StopMultipleJobs, name="StopMultipleJobs"),
# JobStatus's
    url(r"^JobStatus", views.getJobStatus, name="JobStatus"),
# StopStatus's
    url(r"^stopJob", views.stopJob, name="stopJob"),
# SetTopBox 
    url(r"^Set_Top_Box", views.GetSerialNum, name="Set_Top_Box"),

# Test Suite and Cases
    url(r"^test-suite-cases", views.test_suite_cases, name="test_suite_with_cases"),

# testsuite
    url(r"^test_suites/$", views.TestSuiteList.as_view(), name="test_suite_list"),
    url(r'^test_suites/new$', views.TestSuiteCreate.as_view(), name='test_suite_new'),
    url(r'^test_suites/edit/(?P<pk>\d+)/$', views.TestSuiteUpdate.as_view(), name='test_suite_edit'),
    url(r"^test_suites/delete", views.delete_test_suite, name="test_suite_delete"),

# device
    url(r"^devices$", views.DeviceList.as_view(), name="device_list"),
    url(r"^devices/new$", views.DeviceCreate.as_view(), name="device_new"),
    url(r"^devices/delete", views.delete_device, name="device_delete"),
    url(r'^devices/edit/(?P<pk>\d+)/$', views.DeviceUpdate.as_view(), name='device_edit'),

# configs
    url(r"^configs$", views.ConfigList.as_view(), name="config_list"),
    url(r"^configs/new$", views.ConfigCreate.as_view(), name="config_new"),
    url(r"^configs/delete", views.delete_config, name="config_delete"),
    url(r'^configs/edit/(?P<pk>\d+)/$', views.ConfigUpdate.as_view(), name='config_edit'),
    
# TestCase
    url(r'^test-case/$', views.TestCaseList.as_view(), name='test_case_list'),
    url(r'^test-case/new$', views.TestCaseCreate.as_view(), name='test_case_new'),
    url(r'^test-case/edit/(?P<pk>\d+)/$', views.TestCaseUpdate.as_view(), name='test_case_edit'),
    url(r'^test-case/delete', views.delete_test_case, name='test_case_delete'),
]