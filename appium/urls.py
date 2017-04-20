from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.appium_home, name='appium'),
    url(r'^run', views.appium_run_job, name='appium_run'),
    url(r'^console/$', views.consolelink, name='consolelink'),

    
    # JobStatus's
    url(r"^job-status", views.appium_job_status, name="appium_job_status"),

    
    # Test Suite and Cases
    url(r"^android-test-suite-cases", views.appium_android_test_suite_cases, name="appium_android_test_suite_with_cases"),
    url(r"^ios-test-suite-cases", views.appium_ios_test_suite_cases, name="appium_ios_test_suite_with_cases"),

    url(r"^android-devices-list", views.appium_android_devices_list, name="appium_android_devices_list"),
    url(r"^ios-devices-list", views.appium_ios_devices_list, name="appium_ios_devices_list"),

    url(r"^android-test-cases", views.appium_android_test_cases, name="appium_android_test_cases"),
    url(r"^ios-test-cases", views.appium_ios_test_cases, name="appium_ios_test_cases"),

    
    # TestCase Configuration
    url(r'^test-case$', views.AppiumTestCaseList.as_view(), name='appium_test_case_list'),
    url(r'^test-case/new$', views.AppiumTestCaseCreate.as_view(), name='appium_test_case_new'),
    url(r'^test-case/edit/(?P<pk>\d+)/$', views.AppiumTestCaseUpdate.as_view(), name='appium_test_case_edit'),
    url(r'^test-case/delete', views.AppiumTestCaseDelete, name='appium_test_case_delete'),

    # TestSuite Configuration
    url(r"^test-suites$", views.AppiumTestSuiteList.as_view(), name="appium_test_suite_list"),
    url(r'^test-suites/new$', views.AppiumTestSuiteCreate.as_view(), name='appium_test_suite_new'),
    url(r'^test-suites/edit/(?P<pk>\d+)/$', views.AppiumTestSuiteUpdate.as_view(), name='appium_test_suite_edit'),
    url(r"^test-suites/delete", views.AppiumTestSuiteDelete, name="appium_test_suite_delete"),
        
   # Device Configuration
    url(r"^devices$", views.AppiumDeviceList.as_view(), name="appium_device_list"),
    url(r"^devices/new$", views.AppiumDeviceCreate.as_view(), name="appium_device_new"),
    url(r'^devices/edit/(?P<pk>\d+)/$', views.AppiumDeviceUpdate.as_view(), name='appium_device_edit'),
    url(r"^devices/delete", views.AppiumDeviceDelete, name="appium_device_delete"),

 # OS & Versions Configuration
    url(r'^os-version$', views.AppiumOSList.as_view(), name='appium_os_list'),
    url(r'^os-version/new$', views.AppiumOSCreate.as_view(), name='appium_os_new'),
    url(r'^os-version/edit/(?P<pk>\d+)/$', views.AppiumOSUpdate.as_view(), name='appium_os_edit'),
    url(r'^os-version/delete', views.AppiumOSDelete, name='appium_os_delete'),
    
        ]