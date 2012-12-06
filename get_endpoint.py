#!/usr/bin/env python
# -*- coding: utf-8 -*-

from httplib import HTTPConnection
import json

url = "localhost:5000"

token = raw_input("token: ")
tenant = raw_input("tenent: ")
params = '{ "auth":{ "token":{"id": "%s"}, "tenantId": "%s" } }' % (token, tenant)
header = {
  "Content-Type": "application/json",
  "X-Auth-Token": token,
}

session = HTTPConnection(url)
session.request("POST", "/v2.0/tokens", params, header)
endpoint_result = json.load(session.getresponse())
session.close()

print json.dumps(endpoint_result, sort_keys=True, indent=2)

