import frappe
from frappe.utils import now_datetime


def successful_login(login_manager):
    print("Login Hook Executed")

    user = frappe.session.user
    current_time = now_datetime()

    frappe.msgprint(
        msg=f"""
        <b>Login Successful!</b><br><br>
        User: {user}<br>
        Date & Time: {current_time}
        """,
        title="Login Information",
        indicator="green",
    )

    print(f"LOGIN SUCCESS | User: {user} | Time: {current_time}")
    print(login_manager)


def allocate_free_credits(login_manager):
    print("Session Hook Executed")

    user = frappe.session.user
    current_time = now_datetime()

    print(f"SESSION CREATED | User: {user} | Time: {current_time}")

    frappe.msgprint(
        msg=f"""
        <b>Session Created Successfully!</b><br><br>
        User: {user}<br>
        Session Time: {current_time}
        """,
        title="Session Information",
        indicator="blue",
    )


def clear_user_cache(login_manager):
    print("Logout Hook Executed")

    user = frappe.session.user
    current_time = now_datetime()

    print(f"LOGOUT | User: {user} | Time: {current_time}")


def clear_website_cache(path=None):
    if path:
        print(f"WEBSITE CACHE CLEARED FOR: {path}")
    else:
        print("ALL WEBSITE CACHE CLEARED")
