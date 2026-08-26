import frappe
from frappe.search.sqlite_search import SQLiteSearch
class LibraryMemberSearch(SQLiteSearch):

    INDEX_NAME = "library_member_search.db"

    INDEX_SCHEMA = {
        "metadata_fields": ["status"],
        "tokenizer": "unicode61 remove_diacritics 2 tokenchars '-_'",
    }

    INDEXABLE_DOCTYPES = {
        "Library Member": {
            "fields": [
                "name",
                {"title": "first_name"},
                {"content": "email_address"},
                "status",
            ]
        }
    }

    def get_search_filters(self):
        return {}