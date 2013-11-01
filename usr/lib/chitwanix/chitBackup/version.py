#!/usr/bin/python

import apt
import sys

try:
	cache = apt.Cache()	
	pkg = cache["chitbackup"]
	print pkg.installed.version
except:
	pass


