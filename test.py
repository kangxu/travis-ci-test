#!/usr/bin/env python
import os
import os.path
import commands

print "directory:%s" % os.path.abspath(__file__)

#for curdir, subDirs, subFiles in os.walk(os.curdir):
 #print  subFiles,

print commands.getoutput("git ls-tree -r --name-only HEAD")
