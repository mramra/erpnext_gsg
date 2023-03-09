import frappe
def execute():
    frappe.db.sql(""" UPDATE `tabDocField` SET `options`='GSG-JV-.YYYY.-' where fieldname='naming_series' AND parent='payment entry'  """)
#bench migrate