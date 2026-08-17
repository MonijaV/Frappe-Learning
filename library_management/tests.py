import frappe
def before_tests():
    print("BEFORE TESTS HOOK EXECUTED")

    if not frappe.db.exists("Library Member", "Test Member"):
        member = frappe.new_doc("Library Member")
        member.first_name = "Test"
        member.last_name = "Member"
        member.email_address = "test@example.com"
        member.phone = "9876543210"
        member.insert()

        frappe.db.commit()

        print("Test Member created")