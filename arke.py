#!/usr/bin/python

###########################################################
# Arke is a server management tool written in Python      #
# It is designed to perform simple server administration  #
# tasks and alert a sys admin to anything that requires   #
# special attention.                                      #
#                                                         #
# Version: 0.1                                            #
# Author: James Thompson                                  #
#                                                         #
###########################################################

#
# Imports
#
import os, platform, apt
import arke_config as config
from arke_lib import *
from arke_lib import __hostname__

#
# Main Program
#

__version__ = "0.1"
__supported_dists__ = ["Debian", "Ubuntu", "debian", "ubuntu"]

print "Welcome to Arke %s!" % __version__
print " "

# Discover what system we are on, and ensure we are root
dist, vers, name = platform.linux_distribution()
if dist not in __supported_dists__:
	print "Sorry, %s is not supported!" % dist
	exit(0)

print " "
print "Running maintenance tasks..."

# First we update apt
cache=apt.Cache()
cache.update()
cache.open(None)
cache.commit()
cache.upgrade()
pkgs = cache.get_changes()

packageVers = " -> %s" % '\n -> '.join([x.name for x in pkgs])
packageStr = "%d packages need upgrading!" % len(pkgs)
print "%s\n%s" % (packageStr, packageVers)

# What should we do with updates?
if config.auto_update:
	# Print Info
	print 'Upgrading System...'

	# Lets update! Use os for this one..
	os.system("apt-get upgrade --trivial-only")

	# Send mail to notify
	sysmail("The following packages were upgraded on %s!\n%s" % (__hostname__, packageVers))
else:
	# Just send a notification
	sysmail("The following packages require upgrading on %s!\n%s" % (__hostname__, packageVers), subject="Package Upgrades")