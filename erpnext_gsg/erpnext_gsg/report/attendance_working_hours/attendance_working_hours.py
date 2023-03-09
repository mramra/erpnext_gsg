# Copyright (c) 2023, erpnext_gsg and contributors
# For license information, please see license.txt

import copy
from collections import OrderedDict

import frappe
from frappe import _, qb
from frappe.utils import time_diff_in_hours

def execute(filters=None):
	if not filters:
		return [], [], None, []
	columns = get_columns(filters)
	conditions = get_conditions(filters)
	data = get_data(conditions,filters)
	return columns,data

def get_conditions(filters):
	conditions = ""
	if filters.get("from_date") and filters.get("to_date"):
		conditions += "attendance_date between %(from_date)s and %(to_date)s"
	if filters.get("employee"):
		conditions += " and employee in %(employee)s"
	if filters.get("department"):
		conditions += " and department in %(department)s"
	return conditions

def get_data(conditions,filters):
	# nosemgrep
	data = frappe.db.sql("""
		SELECT attendance_date,employee,employee_name,check_in,check_out,name
		FROM `tabAttendance` 
		WHERE {conditions}
		""".format(conditions=conditions),filters,as_dict=1)
	if data[0].check_out and data[0].check_in:
		working_hours=time_diff_in_hours(data[0].check_out,data[0].check_in)
	else:
		working_hours=0
	data[0]["working_hours"]=working_hours
	
	return data


def get_columns(filters):
	columns = [
		{"label": _("Attendance Date"),"fieldname": "attendance_date","fieldtype": "Data"},
		{"label": _("Employee"),"fieldname": "employee","fieldtype": "Data"},
		{"label": _("Employee Name"),"fieldname": "employee_name","fieldtype": "Data"},
		{"label": _("Check in"),"fieldname": "check_in","fieldtype": "Data"},
		{"label": _("Check Out"),"fieldname": "check_out","fieldtype": "Data"},
		{"label": _("Working Hours"),"fieldname": "working_hours","fieldtype": "Data"},
		{"label": _("View Attendance"),"fieldname": "name","fieldtype": "Link","options": "Attendance",},
		
	]
	return columns
