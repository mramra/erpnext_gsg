import frappe
from frappe.model.document import Document
from frappe.utils import time_diff, get_first_day, get_last_day, today

#class EmployeeExcuse(Document):
def validate(self):
        self.hours = time_diff(self.to_time, self.from_time).total_seconds()/3600
        if self.from_time > self.to_time:
            frappe.throw("From Time is After To Time !!")
        excuse_hours_dp = frappe.db.sql(f""" select excuse_hours_alowed from tabDepartment where name = '{self.department}' """)[0][0]
        applied_in_the_month = frappe.db.sql(f""" select hours from tabEmployee Excuse where employee = '{self.employee}' and excuse_date between '{get_first_day(today())}' and '{get_last_day(today())}'""")[0][0]
        if self.hours > excuse_hours_dp - applied_in_the_month:
            frappe.throw("You Have Reached The Limit of Applications in This Month")