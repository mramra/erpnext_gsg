frappe.ui.form.on("Employee Excuse Application", {
    to_time: function(frm) {
        frappe.call({
            method:"erpnext_gsg.erpnext_gsg.doc_event.employee_event.hour",
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