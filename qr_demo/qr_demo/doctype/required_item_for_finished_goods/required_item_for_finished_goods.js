// Copyright (c) 2023, ALYF GmbH and contributors
// For license information, please see license.txt

frappe.ui.form.on('Required Item For Finished Goods', {
	stage   :function(frm) {
        frm.clear_table("item_as_per_bom")
		frm.refresh_field('item_as_per_bom')
		frm.call({
			method:'get_data',
			doc: frm.doc,
		});
	}
})

frappe.ui.form.on('Required Item For Finished Goods', {
	add_entry: function(frm) {
		frm.call({
			method:'append_user_entry',//function name defined in python
			doc: frm.doc, //current document
		});
		frm.refresh_field('entry_catalog')
	}
});


