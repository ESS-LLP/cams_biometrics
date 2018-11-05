# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "cams_biometrics"
app_title = "Cams Biometrics"
app_publisher = "earthians"
app_description = "API to post attendance from CAMS Biometrics"
app_icon = "octicon octicon-clippy"
app_color = "#62f23a"
app_email = "info@earthianslive.com"
app_license = "MIT"

before_install = "cams_biometrics.before_install"


fixtures = [{"dt":"Custom Field", "filters": [["dt", "in", ("Attendance", "HR Settings")]]}]

scheduler_events = {
	"daily": [
		"cams_biometrics.utils.submit_attendance"
	]
}
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/cams_biometrics/css/cams_biometrics.css"
# app_include_js = "/assets/cams_biometrics/js/cams_biometrics.js"

# include js, css files in header of web template
# web_include_css = "/assets/cams_biometrics/css/cams_biometrics.css"
# web_include_js = "/assets/cams_biometrics/js/cams_biometrics.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "cams_biometrics.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "cams_biometrics.install.before_install"
# after_install = "cams_biometrics.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "cams_biometrics.notifications.get_notification_config"

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
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"cams_biometrics.tasks.all"
# 	],
# 	"daily": [
# 		"cams_biometrics.tasks.daily"
# 	],
# 	"hourly": [
# 		"cams_biometrics.tasks.hourly"
# 	],
# 	"weekly": [
# 		"cams_biometrics.tasks.weekly"
# 	]
# 	"monthly": [
# 		"cams_biometrics.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "cams_biometrics.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "cams_biometrics.event.get_events"
# }
