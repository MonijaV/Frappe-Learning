import frappe
@frappe.whitelist()
def custom_get_count(doctype, filters=None, debug=False, cache=False):
    print("=" * 50)
    print("CUSTOM GET COUNT IS RUNNING")
    print("Doctype:", doctype)
    print("Filters:", filters)
    print("=" * 50)

    count = frappe.db.count(doctype, filters=filters)

    return count