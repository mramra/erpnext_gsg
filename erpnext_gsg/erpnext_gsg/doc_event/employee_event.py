import frappe
from frappe.utils import time_diff_in_hours


@frappe.whitelist()
def hour(from_time,to_time):
    return time_diff_in_hours(to_time,from_time)

@frappe.whitelist()
def get_salary(name):
    salery=frappe.db.sql("""select rounded_total , max(creation) from `tabSalary Slip` WHERE `employee`=%s""",name,as_dict=1)
    if salery[0].rounded_total:
        return salery[0].rounded_total
    else:
        return 0

