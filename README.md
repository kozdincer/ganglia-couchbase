ganglia-couchbase
=================

Couchbase Plugin for Ganglia Monitoring

Collects status for one bucket via curl and reports to ganglia

couchbase.pyconf goes to /etc/ganglia/conf.d/
couchbase.py goes to /usr/lib/ganglia/python_modules

Edit the username, password and ipaddress or hostname as well as the bucketname of your couchbase server to observe. 
Typically installed on your couchbase server pointing to itself. My workaround for not supporting multiple buckets
is to run on one couchbase server for one bucket and another for another bucket.

TODO: 
- support more than one bucket, different prefix per bucket 
- make parameter to adjust how many of the data point series you want to average over, right now using all so 
  single spikes in a sea of zeros may get lost
- lower end version for stats that are not bucket specific but just general cluster stats
