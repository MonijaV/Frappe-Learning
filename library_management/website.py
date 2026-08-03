def update_context(context):
    print("Global")
    context.library_name = "Global Library"
    context.hello="Global Hello"

def resolve_path(path):
    print("Resolving:", path)

    if path == "newdemo":
        return "demo"

    return path

import frappe
def extend_page_context(context):
    print("extend_page_context executed")

    context.company_name = "Library Management System"
    context.year = 2026
