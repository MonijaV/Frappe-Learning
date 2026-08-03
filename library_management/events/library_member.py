import frappe

def before_insert(doc, method):
    frappe.msgprint("Executed from hooks.py before_insert")