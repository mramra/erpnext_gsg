import frappe
def execute():
    x=frappe.db.sql(""" SELECT `name` FROM `tabAccount` WHERE `account_number`=5112 """)[0][0]
    Taxes = frappe.new_doc("Purchase Taxes and Charges Template")
    Taxes.title="Purchase Taxes 16%"
    Taxes.is_default=1
    Taxes.append("taxes",{"account_head":x,"rate": 16,"description":x})
    Taxes.insert(ignore_permissions=True)

#bench migrate