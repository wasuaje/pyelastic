#!/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import socket
import simplejson as json

from elasticsearch import Elasticsearch

es = Elasticsearch([  {'host': '10.6.0.225'} ] )


idx= es.search(index="logstash-2015.04.06", fields=["request",], q="request:*.js")
print len(idx)
for i in idx:
	print idx["hits"]

#print json.dumps(idx, sort_keys=True,indent=2)
