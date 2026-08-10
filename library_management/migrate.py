import frappe
from frappe.utils import now_datetime

def before_migrate():
    print("=" * 40)
    print("BEFORE MIGRATE")
    print("Site:", frappe.local.site)
    print("Time:", now_datetime())
    print("=" * 40)


def after_migrate():
    print("=" * 40)
    print("AFTER MIGRATE")
    print("Site:", frappe.local.site)
    print("Time:", now_datetime())
    print("=" * 40)