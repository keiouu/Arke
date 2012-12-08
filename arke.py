#!/usr/bin/python

###########################################################
# Arke is a server management tool written in Python      #
# It is designed to perform simple server administration  #
# tasks and alert a sys admin to anything that requires   #
# special attention.                                      #
#                                                         #
# Version: 0.2                                            #
# Author: James Thompson                                  #
#                                                         #
###########################################################
#                                                         #
# Changelist for v0.2                                     #
#   -> Arke now runs as a Daemon                          #
#   -> Sends notifications to central server              #
#   -> Can accept actions from central server             #
#                                                         #
###########################################################

#
# Imports
#

from src import main

#
# Main Program
#

if __name__ == "__main__":
        daemon = main.Arke('/tmp/arke.pid')
        if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                        daemon.start()
                elif 'stop' == sys.argv[1]:
                        daemon.stop()
                elif 'restart' == sys.argv[1]:
                        daemon.restart()
                else:
                        print "Unknown command"
                        sys.exit(2)
                sys.exit(0)
        else:
                print "usage: %s start|stop|restart" % sys.argv[0]
                sys.exit(2)