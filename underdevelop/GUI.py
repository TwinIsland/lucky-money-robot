#encoding:utf-8
import tkinter as tk
import setting
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import time

window = tk.Tk()
window.title('抢红包机器人')
window.geometry('670x432')
window.resizable(False, False)

menu = tk.Menu(window)

tk.Label(window,text='抢红包机器人',font=('等线',20)).pack(side='top')
command_box = tk.Text(window,height=8,width=800)

group_inf = tk.StringVar()
update = tk.StringVar()
money = 0
revenue = setting.get_setting()['money']

tk.Label(window,text='群聊名称: ',font=('等线',13)).place(x=60,y=80)
tk.Label(window,text='侦测频率: ',font=('等线',13)).place(x=60,y=120)
tk.Entry(window,textvariable=group_inf).place(x=190,y=80)
tk.Entry(window,textvariable=update).place(x=190,y=120)
tk.Label(window,text='目前收益: ',font=('等线',13)).place(x=60,y=180)
tk.Label(window,text='总共收益: ',font=('等线',13)).place(x=60,y=220)
tk.Label(window,text=money,font=('等线',13)).place(x=190,y=180)
tk.Label(window,text=revenue,font=('等线',13)).place(x=190,y=220)


def begin():
    try:
        setting.write_setting(float(update.get()),group_inf.get())
    except Exception:
        command_box.insert('end','>> 【错误】 请检查群聊名称以及侦测频率项目！\n')
        return 0
    try:
        command_box.insert('end','>> 稍等片刻，正在连接至虚拟机...\n')
        poco = AndroidUiautomationPoco()
        poco.device.wake()
        poco(text='微信').click()
        command_box.insert('end', '>> 【成功】 已成功连接至安卓虚拟机！\n')
    except IndexError:
        command_box.insert('end','>> 【错误】 请检查安卓虚拟机的开启情况以及微信的安装情况！\n')
        return 0

    set = setting.get_setting()
    group_name = set['group']
    update_frequency = set['update']
    command_box.insert('end','>> 配置信息: \n群聊名称: ' + group_name +
          '\n更新频率: ' + str(update_frequency) + '\n')

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
        command_box.insert('end','>> 【错误】 不能找到指定群聊！\n')
        return 0
    else:
        command_box.insert('end','>> 【成功】 成功加载群聊信息！\n')

    def is_bao_exist():
        try:
            return not poco("com.tencent.mm:id/ag").child("android.widget.RelativeLayout")[-1].offspring(
                "android.widget.FrameLayout").child("android.widget.LinearLayout").offspring(
                "com.tencent.mm:id/aul").exists()
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

    command_box.insert('end','>> 【成功】 已启动机器人！')

    while (True):
        time.sleep(update_frequency)
        if poco('com.tencent.mm:id/auk').exists():
            if is_bao_exist():
                status = catch_bao(poco('com.tencent.mm:id/auk')[-1])
                if status != 0:
                    command_box.insert('end', ':>> 成功获取红包：' + str(status) + '元！\n')
                    setting.addMoney(status)
                    command_box.insert('end','总共红包收益: ' + str(setting.get_setting()['money']) + '元\n')
                    poco('com.tencent.mm:id/m1').click()
                else:
                    command_box.insert('end','>> 抢红包失败，你朋友手太快了\n')


tk.Button(window,text='启动机器人',command=begin,width=24,height=10,bg='grey').place(x=400,y=50)
command_box.pack(side='bottom')
tk.mainloop()