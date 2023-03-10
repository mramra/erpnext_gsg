import frappe
from frappe.utils import time_diff_in_hours


@frappe.whitelist()
def hour(from_time,to_time):
    return time_diff_in_hours(to_time,from_time)

@frappe.whitelist()
def get_salary(name):
     return 10

