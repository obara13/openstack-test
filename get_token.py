#!/usr/bin/env python
# -*- coding: utf-8 -*-

from getpass import getpass
from httplib import HTTPConnection
import json

user = raw_input("user: ")
password = getpass("password: ")

url = "localhost:5000"
params = '''{
  "auth": {
    "passwordCredentials": {
      "username": "%s",
      "password": "%s"
    }
  }
}''' % (user, password)
header = {
  "Content-Type": "application/json"
}

session = HTTPConnection(url)
session.request("POST", "/v2.0/tokens", params, header)
auth_result = json.load(session.getresponse())
session.close()

print json.dumps(auth_result, sort_keys=True, indent=2)

