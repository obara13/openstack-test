#!/usr/bin/env python
# -*- coding: utf-8 -*-

from httplib import HTTPConnection
import json

token = raw_input("token: ")

url = "localhost:5000"
header = {
  "Content-Type": "application/json",
  "X-Auth-Token": token
}

session = HTTPConnection(url)
session.request("GET", "/v2.0/tenants", "", header)
tenant_result = json.load(session.getresponse())
session.close()

print json.dumps(tenant_result, sort_keys=True, indent=2)

