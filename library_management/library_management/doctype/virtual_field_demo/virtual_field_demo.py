# Copyright (c) 2026, faris and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class VirtualFieldDemo(Document):

    @property
    def full_name(self):
        return f"{self.first_name or ''} {self.last_name or ''}".strip()