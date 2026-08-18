import frappe
def daily_maintenance():
    frappe.log_error(
        title="Daily Maintenence Test",
        message="daily_maintenance() executed successfully"
    )