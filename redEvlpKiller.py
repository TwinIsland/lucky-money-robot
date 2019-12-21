# encoding:utf-8
__author__ = "Wyatt Huang"

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import setting
from airtest.core.api import auto_setup
from airtest.cli.parser import cli_setup
import time
import os

# Connect the Android Stimulator and start WeChat
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android://127.0.0.1:5037/127.0.0.1:7555?cap_method=JAVACAP&&ori_method=ADBORI",
    ])

poco = AndroidUiautomationPoco()
#poco.device.wake()
#poco(text='微信').click()

# Set the setting item
group_inf = input('\ngroup: ')
update_inf = float(input('update frequency: '))
setting.write_setting(update_inf,group_inf)

set = setting.get_setting()
group_name = set['group']
update_frequency = set['update']
print('Setting Information: \nGroup Name: ' + group_name +
      '\nUpdate Frequency: ' + str(update_frequency) + '\n')

get_into_group = 0
group = poco('com.tencent.mm:id/baj') # group hook in WeChat

if not poco('com.tencent.mm:id/ls').exists():
    for each_group in group:
        if each_group.get_text() == group_name:
            each_group.click()
            get_into_group = 1
else:
    get_into_group = 1 # that mean the user is not in main page of WeChat

if not get_into_group:
    print('Cannot find group')
    os._exit(0)
else:
    print('successfully get into the group !')

def is_bao_exist():
    try:
        return not poco("com.tencent.mm:id/ag").child("android.widget.RelativeLayout").offspring("com.tencent.mm:id/aui")[-1].offspring("com.tencent.mm:id/aul").exists()
    except Exception:
        return 0

def catch_bao(poco_element):
    poco_element.click()
    if poco('com.tencent.mm:id/dam').get_text() == '手慢了，红包派完了':
        poco('com.tencent.mm:id/d84').click()
        return 0
    poco('com.tencent.mm:id/dan').click()
    if poco('com.tencent.mm:id/d6v').exists():
        return float(poco('com.tencent.mm:id/d62').get_text())

print('Begin supervice the Red Envelop...')

while (True):
    time.sleep(update_frequency)
    if poco('com.tencent.mm:id/auk').exists():
        if is_bao_exist():
            status = catch_bao(poco('com.tencent.mm:id/auk')[-1])
            if status == 0:
                print('fail')
            else:
                print('Win: ' + str(status))
                setting.addMoney(status)
                print('Total Win: ' + str(setting.get_setting()['money']) + '\n')
                poco('com.tencent.mm:id/m1').click()

