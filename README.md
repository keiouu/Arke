Arke
====

Arke is a server management and monitoring tool.

It currently performs the following functions:
* Updates apt (apt-get update)
* Sends a notification about required upgrades to a sysadmin
* (Optional) Upgrades trivial packages
* (Optional) Self Auto-Updating

Planned Features:
* (Optional) Run ntp update (for openvz admins who cant use ntpd)
* (Optional) Package Synchronization
* (Optional) Service Monitoring


Installation
=====

To install, open console and run:

wget https://raw.github.com/keiouu/Arke/master/arke_setup && chmod u+x ./arke_setup && ./arke_setup