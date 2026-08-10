import frappe
from frappe.contacts.doctype.address.address import Address
class CustomAddress(Address):
    def show_custom_message(self):
        return "This Address is using CustomAddress!"
    def validate(self):
        print("CUSTOM ADDRESS VALIDATE")
        print("STANDARD ADDRESS VALIDATE COMPLETED")