frappe.ui.form.on("To Whom It Concerns", {
    get_salary: function(frm) {
        frappe.call({
            method:"erpnext_gsg.erpnext_gsg.doc_event.employee_event.get_salary",
            args:{name:frm.doc.employee},
            callback: function(r){frm.set_value("salary",r.message);}
        })
		
	},
});