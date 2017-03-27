ganglia-couchbase
=================

Couchbase Plugin for Ganglia Monitoring

Collects status for one bucket via curl and reports to ganglia

couchbase.pyconf goes to /etc/ganglia/conf.d/
couchbase.py goes to /usr/lib/ganglia/python_modules

Edit the username, password and ipaddress or hostname as well as the bucketname  of your couchbase server to observe. 
Typically installed on your couchbase server pointing to itself

TODO: 
- support more than one bucket, different prefix per bucket 
- Need lower end version for stats that are not bucket specific
