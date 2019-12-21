#encoding:gbk
import os
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import time

poco = AndroidUiautomationPoco()
poco.device.wake()
poco(text='微信').click()

# setting there
group_name = '相亲相爱一家人'
update_frequency = 0.5


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


def catch_bao(poco_element):
    poco_element.click()
    if poco('com.tencent.mm:id/dam').get_text() == '手慢了，红包派完了':
        poco('com.tencent.mm:id/d84').click()
        return 0
    poco('com.tencent.mm:id/dan').click()
    if poco('com.tencent.mm:id/d6v').exists():
        return poco('com.tencent.mm:id/d62').get_text() 

def is_bao_exist():
    return not poco("com.tencent.mm:id/ag").child("android.widget.RelativeLayout")[-1].offspring("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.tencent.mm:id/aul").exists()

while (True):
    time.sleep(update_frequency)
    if poco('com.tencent.mm:id/auk').exists():
        if is_bao_exist():
            status = catch_bao(poco('com.tencent.mm:id/auk')[-1])
            if status:
                print(status)
                print(type(status))
                poco('com.tencent.mm:id/m1').click()
            else:
                print('fail')


