// Copyright (c) 2023, erpnext_gsg and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Attendance Working Hours"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"width": "80",
			"reqd": 1,
			"default": frappe.datetime.add_months(frappe.datetime.get_today(), -1),
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"width": "80",
			"reqd": 1,
			"default": frappe.datetime.get_today()
		},
		{
			"fieldname": "employee",
			"label": __("Employee"),
			"fieldtype": "MultiSelectList",
			"width": "80",
			"get_data": function(txt) {
				return frappe.db.get_link_options("Employee", txt);
			},
			"get_query": () =>{
				return {
					filters: { "docstatus": 1 }
				}
			}
		},
		{
			"fieldname": "department",
			"label": __("Department"),
			"fieldtype": "MultiSelectList",
			"width": "80",
			"get_data": function(txt) {
				return frappe.db.get_link_options("Department", txt);
			},
			"get_query": () =>{
				return {
					filters: { "docstatus": 1 }
				}
			}
		}
	],
	"formatter": function (value, row, column, data, default_formatter) {
		value = default_formatter(value, row, column, data);
		
		if (in_list( column.fieldname) && data && data[column.fieldname] > 0) {
			value = "<span style='color:green;'>" + value + "</span>";
		}

		if (column.fieldname == "delay" && data && data[column.fieldname] > 0) {
			value = "<span style='color:red;'>" + value + "</span>";
		}
		return value;
	}
};
