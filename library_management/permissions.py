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


"""def library_member_query(user):
    if not user:
        user = frappe.session.user
    # Test User -> Active members only
    if user == "testuser@example.com":
        return "`tabLibrary Member`.`check` = 'Active'"
    # Reader -> Inactive members only
    elif user == "reader@example.com":
        return "`tabLibrary Member`.`check` = 'Inactive'"
    # Everyone else (Administrator)
    return """""

