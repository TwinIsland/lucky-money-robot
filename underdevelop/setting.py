#encoding:gbk

import json

def get_setting():
    with open('config.evlp','r') as f:
        data = json.loads(f.read())
        f.close()
        return data


def write_setting(update_frequency, group_name):
    money =  get_setting()['money']
    with open('config.evlp','w') as f:
        f.write(json.dumps({
            'update':update_frequency,
            'group':group_name,
            'money':money
        }))
        f.close()

def addMoney(money):
    current_setting = get_setting()
    current_setting['money'] += money
    with open('config.evlp','w') as f:
        f.write(json.dumps(current_setting))
    f.close()

