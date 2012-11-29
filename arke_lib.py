import arke_config
import smtplib, string, os
from socket import gethostname

def sysmail(message):
	my_addr = "Arke@%s" % gethostname()
	body = string.join((
		"From: %s" % my_addr,
		"To: %s", arke_config.email,
		"Subject: [Arke] Notification Received!",
		"",
		message
	), "\r\n")
	server = smtplib.SMTP(arke_config.smtp_host)
	server.sendmail(my_addr, [arke_config.email], body)
	server.quit()
