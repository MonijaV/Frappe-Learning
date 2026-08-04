import frappe

def library_member_permission(doc, user=None, permission_type=None):

    print("\n========== HAS PERMISSION ==========")
    print("User:", user)
    print("Permission Type:", permission_type)
    print("Document:", doc.name)

    if "Library Reader" in frappe.get_roles(user):

        if doc.first_name == "Monisha":
            print("Access Denied")
            return False

    return True