import frappe
from frappe.model.document import Document
from frappe.utils import time_diff, get_first_day, get_last_day, today

#class EmployeeExcuseApplication(Document):
def validate(doc,method):
        if doc.from_time > doc.to_time:
            frappe.throw("ERROR Time !!")
        excuse_hours_dp = frappe.db.sql(f""" select excuse_hours_alowed from tabDepartment where name = '{doc.department}' """)[0][0]
        hours_month = frappe.db.sql(f""" select COUNT(hours) from `tabEmployee Excuse Application` where employee = '{doc.employee}' and excuse_date between '{get_first_day(today())}' and '{get_last_day(today())}'""")[0][0]
        if doc.hours+hours_month > excuse_hours_dp:
            frappe.throw("رصيد الساعات الشهرية ستنفذ")