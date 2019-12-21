# encoding:utf-8
import os
import time
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import setting

poco = AndroidUiautomationPoco()
poco.device.wake()
poco(text='微信').click()

set = setting.get_setting()
group_name = set['group']
update_frequency = set['update']
print('Setting Information: \nGroup Name: ' + group_name +
      '\nUpdate Frequency: ' + str(update_frequency) + '\n')

get_into_group = 0
group = poco('com.tencent.mm:id/baj')

if not poco('com.tencent.mm:id/ls').exists():
    for each_group in group:
        if each_group.get_text() == group_name:
            each_group.click()
            get_into_group = 1
else:
    get_into_group = 1

if not get_into_group:
    print('Cannot find group')
    os._exit(0)
else:
    print('successfully get into the group !')

def is_bao_exist():
    try:
        return not poco("com.tencent.mm:id/ag").child("android.widget.RelativeLayout")[-1].offspring("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.tencent.mm:id/aul").exists()
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
            if status != 0:
                print('Win: ' + str(status))
                setting.addMoney(status)
                print('Total Win: ' + str(setting.get_setting()['money']) + '\n')
                poco('com.tencent.mm:id/m1').click()
            else:
                print('fail')

