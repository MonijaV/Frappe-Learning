import frappe

def custom_logic(doc, method):
    frappe.msgprint("Hook executed!")

"""@frappe.whitelist(allow_guest=True)
def who_am_i():
    return {
        "current_user": frappe.session.user
    }"""


@frappe.whitelist(allow_guest=True)
def signup_user(
    first_name,
    last_name,
    phone,
    email,
    password,
    address,
    occupation
):

    doc = frappe.get_doc({
        "doctype": "Signup User",
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
        "email_address": email,
        "password": password,
        "address": address,
        "occupation": occupation
    })

    doc.insert(ignore_permissions=True)

    return {
        "message": "Signup Successful"
    }



