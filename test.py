#!/usr/bin/env python
import os
import os.path

print "directory:%s" % os.path.abspath(__file__)

for curdir, subDirs, subFiles in os.walk(os.curdir):
  print  subFiles,
