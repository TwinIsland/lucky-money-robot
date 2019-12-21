#encoding:utf-8

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco()
poco.device.wake()
poco(text='微信').click()