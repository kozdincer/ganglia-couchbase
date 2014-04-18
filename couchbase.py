import requests
import random
import json

HOST = ""
NAME = ""
PORT = ""
BCKT = ""
PREFIX = 'cb_'

def get_descriptor(name):
    d = {'name': name,
        'call_back': get_value,
        'time_max': 90, 
        'value_type': 'uint',
        'units': 'C',
        'slope': 'both',
        'format': '%u',
        'description': '%s metric' %name,
        'groups': 'couchbase'} 

    return d

def get_value(name):
    return random.randint(1,100)


def metric_init(params):
    global s
    descriptors = []

    url = 'http://%s:%s/pools/default/buckets/%s/nodes/%s:%s/stats/' %(HOST, PORT, BCKT, NAME, PORT)
    r = requests.get(url, auth=('username', 'password'))
    j = json.loads(r.content)
    s = j['op']['samples']
    for i in s:
        name = PREFIX + str(i)
        #d = get_descriptor(i, int(s[i][0]))
        d = get_descriptor(name)
        descriptors.append(d)

    return descriptors


def metric_cleanup():
    '''Clean up the metric module.'''
    pass


if __name__ == '__main__':
    dd = metric_init({})
    for d in dd:
        print d['name']

