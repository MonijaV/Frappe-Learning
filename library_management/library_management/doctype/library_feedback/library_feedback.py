# Copyright (c) 2026, faris and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class LibraryFeedback(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		attachment: DF.Attach | None
		feedback: DF.SmallText | None
		rating: DF.Rating
		status: DF.Literal["Pending", "Approved"]
		user_email: DF.Data | None
	# end: auto-generated types

	pass
