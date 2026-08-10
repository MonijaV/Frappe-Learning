# Copyright (c) 2026, faris and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document


class LibraryMember(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	"""from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from library_management.library_management.doctype.favourite_book.favourite_book import FavouriteBook
		from library_management.library_management.doctype.member_address.member_address import MemberAddress

		address: DF.Table[MemberAddress]
		check: DF.Literal["Active", "Inactive"]
		email_address: DF.Data | None
		favourite_books: DF.TableMultiSelect[FavouriteBook]
		first_name: DF.Data
		full_name: DF.Data | None
		last_name: DF.Data | None
		naming_series: DF.Literal["LM-.##", "LGM-.##"]
		non_favourite_books: DF.Data | None
		phone: DF.Data
	# end: auto-generated types

	pass"""

	"""def before_insert(self):
		frappe.msgprint("before_insert runs only once like until the doc is submitted,not after that!!")
		if len(str(self.phone))!=10:
			frappe.throw("unvalid phone number")

	def before_naming(self):
		frappe.msgprint(f"Name is: {self.name}")
		self.full_name = f"{self.first_name} {self.last_name}"
		frappe.msgprint("before_naming() executed!!")

	def autoname(self):
		self.name="Member-" + self.full_name
		frappe.msgprint("autoname is executed")

	def before_validate(self):
		self.full_name = f"{self.first_name} {self.last_name}"
		frappe.msgprint("before_validate is executed")

	def validate(self):
		if self.full_name!=self.first_name+" "+self.last_name:
			frappe.throw("Invalid full_name")
		if len(str(self.phone))!=10:
			frappe.throw("Phone number must be ten digits")
		else:
			frappe.msgprint("Validate runs every time!!")

	def before_save(self):
		self.email_address=self.email_address.lower()
		frappe.msgprint("before_save is executed")

	def after_insert(self):
		frappe.msgprint("The document is inserted sucessfully")
		frappe.msgprint(f"Document {self.name} inserted successfully")"""



	


