#
# Storage
#


from pymongo import MongoClient
from src import *
import datetime

connection = MongoClient(config.mongo_host, config.mongo_port)
db = connection[util.hostname()]


# A generic model
class Model(object):

	# Returns the collection
	@property
	def collection(self):
		return db[type(self)]

	# Create a new MongoDB Doc
	def create(self, doc):
		return self.collection.insert(doc)


# A Task to be reviewed or that has been completed
# name
# description
# priority (1-10) 1 is the most important
# type = ["Generic", "Package"]
# status = ["Proposed", "Accepted", "Rejected", "Completed"]
class Task(Model):

	def create(self, name, description="No Description", priority=5, task_type="Package", status="Proposed"):
		Model.create(self, {
			"name": name,
			"description": description,
			"priority": priority,
			"type": task_type,
			"status": status,
			"date": datetime.datetime.utcnow()
		})