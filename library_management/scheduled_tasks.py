import frappe
from frappe.utils import now

def scheduler_demo():
    print("\n==============================")
    print("Scheduler Event is Running")
    print("Current Time:", now())
    print("==============================\n")