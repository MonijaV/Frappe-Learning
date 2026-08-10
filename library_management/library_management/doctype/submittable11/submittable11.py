# Copyright (c) 2026, faris and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class submittable11(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		email: DF.Data | None
		name1: DF.Data | None
		phone: DF.Data | None
	# end: auto-generated types

	pass
