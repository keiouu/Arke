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
		cache.upgrade(True)
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
				new_pkgs = cache.get_changes()
				if len(new_pkgs) > 0:
					# Something went wrong, send a notification
					succeeded = " -> %s" % '\n -> '.join([x.name for x in pkgs if x not in new_pkgs])
					failed = " -> %s" % '\n -> '.join([x.name for x in new_pkgs])
					store.Task.create("Updates Failed", "Succeeded:\n%s\nFailed:\n%s" % (succeeded, failed), 2, "Package", "Fault")
				else:
					# Send notification
					store.Task.create("Software Updated", "Succeeded:\n%s" % packageVers, 10, "Package", "Info")
			else:
				# Just send a notification
				store.Task.create("Updates Available", "Available:\n%s" % packageVers, 3, "Package", "Proposed")

		####################
		# Auto update self #
		####################

		if config.self_update:
			cwd = os.getcwd()
			os.chdir("/opt/arke/")
			os.system("git pull")
			os.chdir(cwd)