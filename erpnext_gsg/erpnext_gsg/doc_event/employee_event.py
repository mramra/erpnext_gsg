import frappe
from frappe.utils import time_diff_in_hours


@frappe.whitelist()
def hours(from_time,to_time):
    return time_diff_in_hours(to_time,from_time)

@frappe.whitelist()
def salary(name):
    return 10

