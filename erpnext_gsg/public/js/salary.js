frappe.ui.form.on("To Whom It Concerns", {
    salary: function(frm) {
        frappe.call({
            method:"erpnext_gsg.erpnext_gsg.doc_event.employee_event.salary",
            args:{
                name:frm.doc.employee
            },
            callback: function(r){
                frm.set_value("salary",r.message);
            }
        })
		
	},
});