from __future__ import print_function

import os.path
import os

from . import AddUsers

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def CreateLabel():
	try:
		# service = build('people', 'v1', credentials=GoogleAuth.creds)

		print('List 1- connection names')
		# results = service.people().connections().list(
		# 	resourceName='people/me',
		# 	pageSize=10,
		# 	personFields='names,emailAddresses').execute()
		# connections = results.get('connections', [])

		# for person in connections:
		# 	names = person.get('names', [])
		# 	if names:
		# 		name = names[0].get('displayName')
		# 		print(name)

	except HttpError as err:
		print(err)

if __name__ == "__CreateLabel__":
	CreateLabel()