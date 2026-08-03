import frappe

def custom_logic(doc, method):
    frappe.msgprint("Hook executed!")

@frappe.whitelist(allow_guest=True)
def who_am_i():
    return {
        "current_user": frappe.session.user
    }