import frappe
def execute():
    x=frappe.db.sql(""" SELECT `name` FROM `tabAccount` WHERE `account_number`=5205 """)[0][0]
    Taxes = frappe.new_doc("Sales Taxes and Charges Template")
    Taxes.title="Sales Taxes 16%"
    Taxes.is_default=1
    Taxes.append("taxes",{"charge_type":"On Net Total","account_head":x,"rate": 16,"description":x})
    Taxes.insert(ignore_permissions=True)

#bench migrate