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

from frappe.query_builder import DocType
@frappe.whitelist()
def api():
    LibraryMembership=DocType("Library Membership")
    LibraryMember=DocType("Library Member")

    #QUERYBUILDER
    query=(frappe.qb.from_(LibraryMembership).join(LibraryMember).on(LibraryMembership.library_member == LibraryMember.name)
    .select(LibraryMembership.name.as_("membership_name"),LibraryMember.name.as_("member_name"),LibraryMember.first_name,LibraryMember.last_name,LibraryMember.phone).limit(5))
    results=query.run(as_dict=True)

    if not results:
        return {"message":"No records found","data":[]}

    #DOCUMENTAPI
    first_record=frappe.get_doc("Library Member",results[0].member_name)

    first_record.check="Inactive"
    first_record.save()

    #DATABASEAPI
    for row in results:
        member_name = row["member_name"]
        last_name = row["last_name"]
        if last_name:
            new_last_name=last_name.upper()
            frappe.db.set_value("Library Member",member_name,"last_name",new_last_name)
    frappe.db.commit()
    return results


from library_management.search import LibraryMemberSearch
@frappe.whitelist()
def search_library_members(query):

    search = LibraryMemberSearch()

    return search.search(query)





    


    

    




