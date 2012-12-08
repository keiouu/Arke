#####################
# Main Arke Program #
#####################


#
# Imports
#

import os, sys, platform, time, apt
from src import *
from util import *
from util import __hostname__


#
# Main Program
#

class Arke(daemon.Daemon):
	def run(self):
		while True:
			self.perform()
			time.sleep(config.interval) # Run every minute

	def perform(self):__version__ = "0.2"
		__supported_dists__ = ["Debian", "Ubuntu", "debian", "ubuntu"]

		print "Welcome to Arke %s!" % __version__
		print " "

		# Discover what system we are on
		dist, vers, name = platform.linux_distribution()
		if dist not in __supported_dists__:
			sys.exit("\nSorry, %s is not supported!\n" % dist)

		# Ensure we are root
		if not os.geteuid() == 0:
			sys.exit("\nThis script must be run as root!\n")

		print " "
		print "Running maintenance tasks..."

		#################
		# Update System #
		#################

		# First we update apt
		cache = apt.Cache()
		cache.update()
		cache.open(None)
		cache.commit()
		cache.upgrade()
		pkgs = cache.get_changes()

		packageVers = " -> %s" % '\n -> '.join([x.name for x in pkgs])
		packageStr = "%d packages need upgrading!" % len(pkgs)
		print "%s\n%s" % (packageStr, packageVers)

		if len(pkgs) > 0:
			# What should we do with updates?
			if config.auto_update:
				# Print Info
				print 'Upgrading System...'

				# Lets update!
				cache.commit()

				# Send mail to notify
				sysmail("The following packages were upgraded on %s!\n%s" % (__hostname__, packageVers))
			else:
				# Just send a notification
				sysmail("The following packages require upgrading on %s!\n%s" % (__hostname__, packageVers), subject="Package Upgrades")

		####################
		# Auto update self #
		####################

		if config.self_update:
			cwd = os.getcwd()
			os.chdir("/opt/arke/")
			os.system("git pull")
			os.chdir(cwd)