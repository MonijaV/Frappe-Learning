# Copyright (c) 2026, faris and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class SignupUser(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		address: DF.Data | None
		email_address: DF.Data | None
		first_name: DF.Data | None
		last_name: DF.Data | None
		occupation: DF.Literal["Student", "Employee", "Teacher", "Business", "Other"]
		password: DF.Password | None
		phone: DF.Data | None
	# end: auto-generated types

	pass
