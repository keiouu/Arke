#####################
# Main Arke Program #
#####################


#
# Imports
#

import os, time, apt
from src import *


#
# Main Program
#

class Arke(daemon.Daemon):
	def run(self):
		print "\nWelcome to Arke v0.2!\n"

		while True:
			self.perform()
			time.sleep(config.interval)

	# Perform's job is to update and create tasks
	def perform(self):
		print "Running tasks..."

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
				util.sysmail("The following packages were upgraded on %s!\n%s" % (util.hostname(), packageVers))
			else:
				# Just send a notification
				util.sysmail("The following packages require upgrading on %s!\n%s" % (util.hostname(), packageVers), subject="Package Upgrades")

		####################
		# Auto update self #
		####################

		if config.self_update:
			cwd = os.getcwd()
			os.chdir("/opt/arke/")
			os.system("git pull")
			os.chdir(cwd)