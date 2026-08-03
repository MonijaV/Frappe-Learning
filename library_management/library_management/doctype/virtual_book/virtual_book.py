# Copyright (c) 2026, faris and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import os
import json
import frappe


class VirtualBook(Document):
	DATA_FILE = os.path.join(
    os.path.dirname(__file__),
    "data_file.json")

	def db_insert(self, *args, **kwargs):
		raise NotImplementedError

	def load_from_db(self, *args, **kwargs):
		raise NotImplementedError

	def db_update(self, *args, **kwargs):
		raise NotImplementedError

	def delete(self, *args, **kwargs):
		raise NotImplementedError
	
	@staticmethod
	def get_current_data():
		if not os.path.exists(VirtualBook.DATA_FILE):
			return {}
		with open(VirtualBook.DATA_FILE) as f:
			return json.load(f)

	@staticmethod
	def get_list(filters=None, page_length=20, **kwargs):
		pass

	@staticmethod
	def get_count(filters=None, **kwargs):
		pass

	@staticmethod
	def get_stats(**kwargs):
		pass

