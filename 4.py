#!/usr/bin/env python

import re
import httplib

conn = httplib.HTTPConnection('www.pythonchallenge.com')

nums = [12345]
r = re.compile('next nothing is (\d+)')

def get_next(n):
  conn.request('GET', '/pc/def/linkedlist.php?nothing=%d' % n)
  return int(r.findall(conn.getresponse().read())[0])

for i in range(1000):
  print i
  nums.append(get_next(nums[i]))
  print nums

