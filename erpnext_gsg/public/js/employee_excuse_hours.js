frappe.ui.form.on("Employee Excuse Application", {
    hours: function(frm) {
        frappe.call({
            method:"erpnext_gsg.erpnext_gsg.doc_event.employee_event.hours",
            args:{
                from_time:frm.doc.from_time,
                to_time:frm.doc.to_time
            },
            callback: function(r){
                frm.set_value("hours",r.message);
            }
        })
		
	},
});