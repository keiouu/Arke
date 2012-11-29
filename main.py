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
import os, platform
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
os.system("apt-get update")

# What should we do with updates?
if config.auto_update:
	# Lets update!
	os.system("apt-get upgrade --trivial-only")
	# Send mail to notify
	sysmail("Packages were upgraded on %s!" % __hostname__)
else:
	# Just send a notification
	sysmail("Packages require upgrading on %s!" % __hostname__, subject="Package Upgrades")
