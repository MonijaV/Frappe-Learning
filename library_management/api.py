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
# from frappe.utils import now
# @frappe.whitelist()
# def get_recent_todos():
#     todos = frappe.get_list(
#         "ToDo",
#         fields=["name", "description", "owner"],
#         order_by="creation desc",
#         limit_page_length=5,
#     )
#     for todo in todos:
#         todo["owner_email"] = frappe.db.get_value(
#             "User",
#             todo["owner"],
#             "email"
#         )
#     timestamp = now()
#     return {
#         "timestamp": timestamp,
#         "records": todos
#     }

#REALTIME CHART API
# @frappe.whitelist()
# def send_chart_data():
#     data = {
#         "label": 1,
#         "points": [10]
#     }

#     frappe.publish_realtime(
#         "library_chart_update",
#         data
#     )

#LOGGING
# frappe.utils.logger.set_log_level("DEBUG")
# logger = frappe.logger(
#     "library_api",
#     allow_site=True,
#     file_count=10
# )
# @frappe.whitelist()
# def test_logging():
#     user = frappe.session.user
#     logger.debug(f"DEBUG: {user} entered test_logging")
#     logger.info(f"INFO: {user} called test_logging")
#     logger.warning(f"WARNING: test warning for {user}")
#     logger.error(f"ERROR: test error for {user}")
#     return "Logging test completed"



#JS FRAPPECALL ASSIGNMENT
# @frappe.whitelist()
# def create_task(task_subject):
#     task = frappe.new_doc("Task")
#     task.subject = task_subject
#     task.save()

#     return task.name






    


    

    




