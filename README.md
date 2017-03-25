ganglia-couchbase
=================

Couchbase Plugin for Ganglia Monitoring

Collects status for one bucket via curl

couchbase.pyconf goes to /etc/ganglia/conf.d/
couchbase.py goes to /usr/lib/ganglia/python_modules

TODO: 
- support more than one bucket, different prefix per bucket 
- pass username and password etc through params in couchbase.pyconf
- Need lower end version for stats that are not bucket specific
