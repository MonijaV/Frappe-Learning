app_name = "library_management"
app_title = "Library Management"
app_publisher = "faris"
app_description = "library management system"
app_email = "faris@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "library_management",
# 		"logo": "/assets/library_management/logo.png",
# 		"title": "Library Management",
# 		"route": "/library_management",
# 		"has_permission": "library_management.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/library_management/css/library_management.css"
# app_include_js = "/assets/library_management/js/library_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/library_management/css/library_management.css"
# web_include_js = "/assets/library_management/js/library_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "library_management/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "library_management/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "library_management.utils.jinja_methods",
# 	"filters": "library_management.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "library_management.install.before_install"
# after_install = "library_management.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "library_management.uninstall.before_uninstall"
# after_uninstall = "library_management.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "library_management.utils.before_app_install"
# after_app_install = "library_management.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "library_management.utils.before_app_uninstall"
# after_app_uninstall = "library_management.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "library_management.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "library_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"library_management.tasks.all"
# 	],
# 	"daily": [
# 		"library_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"library_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"library_management.tasks.weekly"
# 	],
# 	"monthly": [
# 		"library_management.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "library_management.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "library_management.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "library_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "library_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["library_management.utils.before_request"]
# after_request = ["library_management.utils.after_request"]

# Job Events
# ----------
# before_job = ["library_management.utils.before_job"]
# after_job = ["library_management.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"library_management.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

export_python_type_annotations = True
#app_include_js = "custom_desk.bundle.js
fixtures = [
    "Client Script",
    "Server Script",
    "Web Form"
]
"""app_include_js = [
    "/assets/library_management/js/global_script.js"
]
app_include_css = [
    "/assets/library_management/css/global_style.css"
]

page_js = {
    "permission-manager": "public/js/permission_manager.js"
}

doctype_js = {
    "Library Member": "public/js/library_member.js"
}

doctype_list_js = {
    "Library Member": "public/js/library_member_list.js"
}

website_route_rules = [
    {"from_route": "/books", "to_route": "app"}
]

doc_events = {
    "Library Member": {
        "before_insert": "library_management.events.library_member.before_insert"
    }
}

has_permission = {
    "Library Member":
        "library_management.permissions.library_member.has_permission"
}

doc_events = {
    "ToDo": {
        "validate": "library_management.api.custom_logic"
    }
}"""

#home_page = "about-library"

update_website_context = "library_management.website.update_context"

"""website_route_rules = [
    {"from_route": "/newdemo", "to_route": "demo"}
]"""

"""website_path_resolver = (
    "library_management.website.resolve_path"
)"""

#website_catch_all = "not_found"

"""extend_website_page_controller_context = (
    "library_management.website.extend_page_context"
)"""

#web_include_js = "/assets/library_management/js/portal.js"

#web_include_css = "/assets/library_management/css/portal.css"

"""webform_include_js = {
    "Book Issue": "public/js/book_issue.js"
}

webform_include_css = {
    "Book Issue": "public/css/book_issue.css"
}"""

on_login = "library_management.overrides.successful_login"

on_session_creation = "library_management.overrides.allocate_free_credits"

on_logout = "library_management.overrides.clear_user_cache"

auth_hooks = [
    "library_management.overrides.validate_custom_auth"
]

