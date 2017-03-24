ganglia-couchbase
=================

Couchbase Plugin for Ganglia Monitoring

In the future will collect stats for individual bucket, currently just 
pulls all data point names in a curl call and then randomly fakes data
for them.

couchbase.pyconf goes to /etc/ganglia/conf.d/
couchbase.py goes to /usr/lib/ganglia/python_modules

TODO: 
Collect actual stats instead of randomly generating fake data, use tcpconn module 
as an example on how to collect data in separate worker thread and have callbacks
read them out of the collected data structure.
prefix metric with bucket name to monitor multiple buckets ? 
Currently still need to hardcode username and password in couchbase.py
Need lower end version for stats that are not bucket specific
