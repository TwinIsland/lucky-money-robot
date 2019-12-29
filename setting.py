#encoding:utf-8

import json

def get_money():
    with open('money.evlp','r') as f:
        data = json.loads(f.read())
        f.close()
        return data['money']

def addMoney(money):
    current_setting = get_money()
    current_setting += money
    with open('money.evlp','w') as f:
        f.write(json.dumps({"money": current_setting}))
    f.close()

'''
def write_setting(update_frequency, group_name):
    money =  get_setting()['money']
    with open('money.evlp','w') as f:
        f.write(json.dumps({
            'update':update_frequency,
            'group':group_name,
            'money':money
        }))
        f.close()
'''

