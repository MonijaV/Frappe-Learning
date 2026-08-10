# Copyright (c) 2026, faris and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class MemberLibrary(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		email: DF.Data | None
		first_name: DF.Data | None
		last_name: DF.Data | None
		phone: DF.Data | None
		status: DF.Literal["Active", "Inactive"]
	# end: auto-generated types

	pass
