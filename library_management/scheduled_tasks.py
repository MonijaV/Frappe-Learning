import frappe
from frappe.utils import now

def scheduler_demo():
    print("\n==============================")
    print("Scheduler Event is Running")
    print("Current Time:", now())
    print("==============================\n")


from frappe.utils import now_datetime
def test_configurable_scheduler():
    print("====================================")
    print("CONFIGURABLE SCHEDULER EXECUTED")
    print(f"Time: {now_datetime()}")
    print("====================================")
    frappe.log_error(
        title="Configurable Scheduler Test",
        message=f"Scheduler executed at {now_datetime()}")