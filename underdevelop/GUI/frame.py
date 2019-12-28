#encoding:utf-8
__author__ = "Wyatt Huang"

import tkinter as tk
import setting
import underdevelop.GUI_test.core as core
import threading
import time

window = tk.Tk()
window.title('抢红包机器人')
window.geometry('670x432')
window.resizable(False, False)

menu = tk.Menu(window)

tk.Label(window,text='抢红包机器人',font=('等线',20)).pack(side='top')
command_box = tk.Text(window,height=10,width=800)

group_inf = tk.StringVar()
update = tk.StringVar()
revenue = tk.StringVar()
revenue.set(str(setting.get_setting()['money']))

tk.Label(window,text='群聊名称: ',font=('等线',13)).place(x=60,y=80)
tk.Label(window,text='侦测频率: ',font=('等线',13)).place(x=60,y=120)
tk.Entry(window,textvariable=group_inf).place(x=190,y=80)
tk.Entry(window,textvariable=update).place(x=190,y=120)
tk.Label(window,text='总共收益: ',font=('等线',13)).place(x=60,y=180)
tk.Label(window,text=revenue.get() + ' RMB',font=('等线',13)).place(x=190,y=180)


def write_command(string):
    command_box.insert('end',str(string) + '\n')


def update_revenue():
    while True:
        time.sleep(0.5)
        revenue.set(str(setting.get_setting()['money']))


def begin():
    global StatusRun
    if group_inf.get() == '' or update.get() == '':
        write_command('>> 【错误】 请检查”群聊名称“以及”侦测频率“项目')
    else:
        try:
            write_command('>> 【成功】 已开启机器人！')
            threading.Thread(target=update_revenue,args=()).start()
            threading.Thread(target=core.begin, args=(group_inf.get(), float(update.get()))).start()
            while StatusRun:
                time.sleep(5)
                pass
            else:
                write_command('【错误】 核心线程意外退出！')

        except Exception as e:
            write_command('>> 【错误】 ' + str(e))


tk.Button(window,text='启动机器人',command=begin,width=24,height=7,bg='grey').place(x=400,y=50)
command_box.pack(side='bottom')
tk.mainloop()

