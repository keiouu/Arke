# Arke config handler


import arke_config

defaults = {
	"interval": 14400,
	"auto_update": False,
	"self_update": True,
	"email": "you@you.com",
	"smtp_host": "localhost",
}

class Config(object):
	def __getattr__(self, name):
		try:
			result = getattr(arke_config, name)
			return result
		except AttributeError:
			pass

		if name in defaults:
			return defaults[name]

		raise AttributeError("No default exists for config: %r" % name)