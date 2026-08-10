import frappe
def boot_session(bootinfo):

    bootinfo.library_name = "ABC Library"

    bootinfo.library_timings = "9 AM - 6 PM"

    bootinfo.max_books = 5

    bootinfo.developer = "Monisha"

    bootinfo.current_user = frappe.session.user

    bootinfo.roles = frappe.get_roles()

    bootinfo.current_time = frappe.utils.now()