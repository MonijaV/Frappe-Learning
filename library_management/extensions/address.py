"""import frappe
from frappe.model.document import Document
class AddressMixin(Document):
    @property
    def full_address(self):
        return ", ".join(
            filter(
                None,
                [
                    self.address_line1,
                    self.address_line2,
                    self.city,
                    self.state,
                    self.country,
                    self.pincode
                ]
            )
        )
    def show_address_info(self):
        return f"Address belongs to {self.name}"
    def custom_validation(self):
        print("CUSTOM VALIDATION FROM MIXIN")
    def validate(self):
        super().validate()
        self.custom_validation()
        if not self.phone:
            frappe.throw("Phone Number is required.")"""