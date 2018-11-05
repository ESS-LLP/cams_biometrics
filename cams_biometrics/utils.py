import frappe
from frappe.utils import getdate, flt, time_diff, get_datetime_str, add_days
from werkzeug.wrappers import Response
import pytz
from datetime import datetime

@frappe.whitelist(allow_guest=True)
def mark_attendance(**args):
	args = frappe._dict(args)
	employee = args.get("userid")
	posix_timestamp = args.get("att_time")
	att_type = args.get("att_type")
	stgid = args.get("stgid")
	token = args.get("auth_token")
	# create the custom response
	response = Response()
	response.mimetype = 'text/plain'
	response.charset = 'utf-8'
	response.data = "ok"

	if not employee or not posix_timestamp or not stgid or not token:
		log_error("invalid data", args)
		return response
	# TODO validate URL/IP if provided
	if not frappe.db.exists("Custom Biometric Unit Integration Settings", {"device_id": stgid}):
		log_error("settings for device missing", args)
		return response
	auth_token = frappe.db.get_value("Custom Biometric Unit Integration Settings", {"device_id": stgid}, "auth_token")
	if not auth_token or (auth_token and auth_token != token):
		log_error("device auth error", args)
		return response
	if not frappe.db.exists("Employee", employee):
		log_error("employee not found", args)
		return response
	try:
		timestamp = float(posix_timestamp)
		tz = pytz.timezone('UTC')
		dt = datetime.fromtimestamp(timestamp, tz)
		dt = get_datetime_str(dt)
		date = getdate(dt)
	except:
		log_error("invalid timestamp", args)
		return response
	attendance = None
	company = frappe.db.get_value("Employee", employee, "company")
	attendance_name = frappe.db.exists("Attendance", {"employee": employee, "attendance_date": date})
	if attendance_name:
		attendance = frappe.get_doc("Attendance", attendance_name)

	if attendance:
		if attendance.docstatus == 1:
			log_error("attendance already submitted", args)
			return response
		else:
			attendance.cams_out = dt
			attendance.cams_out_device = stgid
	else:
		try:
			attendance = frappe.get_doc({"doctype": "Attendance",
				"employee": employee,
				"attendance_date": date,
				"company": company,
				"status": "Present",
				"cams_in": dt,
				"cams_in_device": stgid,
				"cams_spend": None
			}).insert(ignore_permissions=1)
			frappe.db.commit()
			return response
		except:
			log_error("insert attendance", args)
			return response

	if attendance.cams_in and attendance.cams_out:
		attendance.cams_spend = time_diff(attendance.cams_out, attendance.cams_in)
	try:
		attendance.db_update()
		frappe.db.commit()
	except:
		log_error("update attendance", args)
		return response
	return response


def log_error(method, message):
	employee = message["userid"]
	message = frappe.utils.cstr(message) + "\n" if message else ""
	d = frappe.new_doc("Error Log")
	d.method = method
	d.error = message
	d.insert(ignore_permissions=True)
	if employee:
		user = frappe.db.get_value("Employee", employee, "user_id")
		if user:
			frappe.get_doc({
				"doctype": "ToDo",
				"description": "Failed to update attendance<br>" + method + "<br>"+ message,
				"owner": user,
				"status": "Open"}
			).insert(ignore_permissions=True)
			frappe.db.commit()

def submit_attendance():
	attendances = frappe.get_all("Attendance", {
		"docstatus": 0,
		"attendance_date": add_days(getdate(), -1)
	})
	for attendance in attendances:
		att_obj = frappe.get_doc("Attendance", attendance["name"])
		att_obj.submit()
	if attendances:
		frappe.db.commit()
