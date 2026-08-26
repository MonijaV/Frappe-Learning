import frappe

# def custom_logic(doc, method):
#     frappe.msgprint("Hook executed!")

# """@frappe.whitelist(allow_guest=True)
# def who_am_i():
#     return {
#         "current_user": frappe.session.user
#     }"""


# @frappe.whitelist(allow_guest=True)
# def signup_user(
#     first_name,
#     last_name,
#     phone,
#     email,
#     password,
#     address,
#     occupation
# ):

#     doc = frappe.get_doc({
#         "doctype": "Signup User",
#         "first_name": first_name,
#         "last_name": last_name,
#         "phone": phone,
#         "email_address": email,
#         "password": password,
#         "address": address,
#         "occupation": occupation
#     })

#     doc.insert(ignore_permissions=True)

#     return {
#         "message": "Signup Successful"
#     }


# PYTHON API ASSIGNMENT

# from frappe.query_builder import DocType
# @frappe.whitelist()
# def api():
#     LibraryMembership=DocType("Library Membership")
#     LibraryMember=DocType("Library Member")

#     #QUERYBUILDER
#     query=(frappe.qb.from_(LibraryMembership).join(LibraryMember).on(LibraryMembership.library_member == LibraryMember.name)
#     .select(LibraryMembership.name.as_("membership_name"),LibraryMember.name.as_("member_name"),LibraryMember.first_name,LibraryMember.last_name,LibraryMember.phone).limit(5))
#     results=query.run(as_dict=True)

#     if not results:
#         return {"message":"No records found","data":[]}

#     #DOCUMENTAPI
#     first_record=frappe.get_doc("Library Member",results[0].member_name)

#     first_record.check="Inactive"
#     first_record.save()

#     #DATABASEAPI
#     for row in results:
#         member_name = row["member_name"]
#         last_name = row["last_name"]
#         if last_name:
#             new_last_name=last_name.upper()
#             frappe.db.set_value("Library Member",member_name,"last_name",new_last_name)
#     frappe.db.commit()
#     return results


# SQLITE SEARCH FULLTEXT FRAMEWORK

# from library_management.search import LibraryMemberSearch
# @frappe.whitelist()
# def search_library_members(query):

#     search = LibraryMemberSearch()

#     return search.search(query)


# PYTHON API UTILITIES ASSIGNMENT
from frappe.utils import now
@frappe.whitelist()
def get_recent_todos():
    # 1. Securely fetch the 5 most recently created ToDos
    todos = frappe.get_list(
        "ToDo",
        fields=["name", "description", "owner"],
        order_by="creation desc",
        limit_page_length=5,
    )

    # 2. Fetch owner's email using frappe.db.get_value()
    for todo in todos:
        todo["owner_email"] = frappe.db.get_value(
            "User",
            todo["owner"],
            "email"
        )

    # 3. Get current server time
    timestamp = now()

    # 4. Return the response
    return {
        "timestamp": timestamp,
        "records": todos
    }





    


    

    




