# metric_init 
#  calls couchbase to get list of metrics with first set of values, 
#  generates descriptors from it with callbacks that can extract one value from global data
#  spawns thread that will collect more data over time updating the global data

import thread
import time
import requests
import json

global url, samples, prefix, refresh_rate


def get_data_for(name):
    global samples, lock, prefix

    unprefixed_name=name[len(prefix):]

    lock.acquire()
    print samples[unprefixed_name]
    ret = int( sum(samples[unprefixed_name]) / len(samples[unprefixed_name]) )
    lock.release()
    return ret

def make_descriptor(name):
    d = {'name': name,
        'call_back': get_data_for,
        'time_max': 90, 
        'value_type': 'uint',
        'units': 'C',
        'slope': 'both',
        'format': '%u',
        'description': '%s metric' %name,
        'groups': 'couchbase'} 

    return d

def make_descriptors():
   global samples, lock, prefix

   descriptors = []

   lock.acquire()

   for key in samples:
       name = prefix + str(key)
       d = make_descriptor(name)
       descriptors.append(d)

   lock.release() 

   return descriptors

def pull_samples_from_couchbase():
   global samples, lock, username, password

   r = requests.get(url, auth=(username, password))

   j = json.loads(r.content)
   s = j['op']['samples']

   lock.acquire()

   samples = s.copy()
   
   lock.release() 


def thread_data_collector(name, refresh_rate):

    while 1: 
       pull_samples_from_couchbase()
       time.sleep(refresh_rate)

def metric_init(params):
    '''Initialize the couchbase metric module and create the 
    metric definition dictionary object for each metric it finds.'''
    global refresh_rate, url, samples, lock, username, password, prefix

    lock = thread.allocate_lock()

    host = ""
    port = 1234
    bucket = ""
    
    #Read parameters provided by gmond.conf 
    if 'host' in params:
        host = params['host']
    if 'port' in params:
        port = int(params['port'])
    if 'bucket' in params:
        bucket = params['bucket']
    if 'prefix' in params:
        prefix= params['prefix']
    if 'refresh_rate' in params:
        refresh_rate = int(params['refresh_rate'])
    if 'username' in params:
        username= params['username']
    if 'password' in params:
        password= params['password']
    
    url = 'http://%s:%s/pools/default/buckets/%s/nodes/%s:%s/stats/' %(host, port, bucket, host, port)

    pull_samples_from_couchbase()

    descriptors = make_descriptors()

    thread.start_new_thread( thread_data_collector, ("data_collector", refresh_rate ) )

    #Return the metric descriptions to Gmond and let it handle the rest
    return descriptors

def metric_cleanup():
    '''Clean up the metric module.'''
    pass

#This code is for debugging and unit testing    
if __name__ == '__main__':
    global url, lock, samples
    params = {'refresh_rate': '20', 'host':'10.0.0.1', 'port':'8091', 'bucket':'default', 'prefix':'cb_', 'username':'ganglia', 'password':'gasecret'}

    print "calling init"
    metric_init(params)
    print "init done, url is %s" %(url)
    print "observing just one of the metrics here for testing, cb_ops"
    while 1:
      print "sleep 3"
      time.sleep(3)
      print get_data_for('cb_ops')
    
    print "done for this test"
