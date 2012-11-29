import arke_config as config
import smtplib, string, os
from socket import gethostname

def sysmail(message):
	my_addr = "Arke@%s" % gethostname()
	body = string.join((
		"From: %s" % my_addr,
		"To: %s" % config.email,
		"Subject: [Arke] Notification Received!",
		"",
		message
	), "\r\n")
	server = smtplib.SMTP(config.smtp_host)
	server.sendmail(my_addr, [config.email], body)
	server.quit()
