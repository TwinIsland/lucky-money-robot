# -*- encoding=utf8 -*-
__author__ = "new"

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android://127.0.0.1:5037/127.0.0.1:7555?cap_method=JAVACAP&&ori_method=ADBORI",
    ])

poco = AndroidUiautomationPoco()

# script content
def is_bao_exist():
    return not poco("com.tencent.mm:id/ag").child("android.widget.RelativeLayout").offspring("com.tencent.mm:id/aui")[-1].offspring("com.tencent.mm:id/aul").exists()

    
print(is_bao_exist())

 