import frappe

def clear_cache():
    print("LIBRARY MANAGEMENT CACHE CLEARED")

    frappe.cache().hdel("library_management_test")