import frappe
def creat_stock_entry(doc,method):  
    if doc.material_request_type=="Material Issue":
        stock_entry_doc=frappe.new_doc("Stock Entry")
        stock_entry_doc.purpose=doc.material_request_type
        stock_entry_doc.stock_entry_type="Material Issue"
        for item in doc.items :
            stock_entry_doc.append("items",{"material_request":item.parent,
                                            "material_request_item": item.name,
                                            "item_code":item.item_code,
                                            "qty":item.qty,
                                            "s_warehouse":item.warehouse})
        stock_entry_doc.insert(ignore_permissions=True)
        stock_entry_doc.submit()