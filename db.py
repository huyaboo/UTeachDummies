"""
Database

Format

/servers/<server id>
	Entry for a server.
	Maybe store some kind of settings?

	fields:
		category: int
			id of channel category to place role channels under


/servers/<server id>/roles/<role id>
	Roles the bot will assign.

	fields:
		channel: int
			id of private text channel for this role
"""

import firebase_admin as admin
import firebase_admin.firestore
from google.cloud import firestore
from dotenv import load_dotenv
from typing import Dict


class SubDb:
	def __init__(self, client: firestore.Client, id: int):
		self.client = client
		self.doc = self.client.collection('servers').document(str(id))

	def create(self, category: int) -> 'SubDb':
		self.doc.set({'category': category})
		return self

	def set_roles(self, roles: Dict[int, int]):
		for role, channel in roles.items():
			self.doc.collection('roles').document(str(role)).set({'channel': channel})


class Db:
	def __init__(self, app: admin.App):
		self.app = app
		self.client: firestore.Client = admin.firestore.client(self.app)

	def server(self, id: int) -> SubDb:
		return SubDb(self.client, id)


def main():
	load_dotenv()
	app = admin.initialize_app()

	db = Db(app)

	print(app.name)
	print(app.project_id)


if __name__ == '__main__':
	main()
