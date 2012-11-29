import arke_config as config
import smtplib, string, os
from socket import gethostname

def hostname():
	return gethostname()

def sysmail(message, subject="Notification Received!"):
	my_addr = "Arke@%s" % gethostname()
	body = string.join((
		"From: %s" % my_addr,
		"To: %s" % config.email,
		"Subject: [Arke] %s" % subject,
		"",
		message
	), "\r\n")
	server = smtplib.SMTP(config.smtp_host)
	server.sendmail(my_addr, [config.email], body)
	server.quit()
