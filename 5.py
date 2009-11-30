#!/usr/bin/env python

"""
URL: http://www.pythonchallenge.com/pc/def/peak.html
"""

import re
import httplib
import pickle

url = "http://www.pythonchallenge.com/pc/def/banner.p"

conn = httplib.HTTPConnection('www.pythonchallenge.com')
conn.request("GET", '/pc/def/banner.p')

p = pickle.loads(conn.getresponse().read())

for l in p:
  line = ""
  for item in l:
    line = line + item[0]*item[1]
  print line

