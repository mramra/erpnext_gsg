import frappe
def execute():
     frappe.db.sql("""UPDATE `tabDocField` SET `options`='Journal Entry
Bank Entry
Cash Entry
Credit Card Entry
Debit Note
Credit Note
Contra Entry
Excise Entry
Write Off Entry
Opening Entry
Depreciation Entry
Exchange Rate Revaluation
Deferred Revenue' where parent='Journal Entry' and fieldname='voucher_type' """)
#bench migrate