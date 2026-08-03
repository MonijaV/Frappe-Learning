import frappe

def on_login(login_manager):
    frappe.logger().info("User Logged In")
    frappe.msgprint("the user is logged in successfully")