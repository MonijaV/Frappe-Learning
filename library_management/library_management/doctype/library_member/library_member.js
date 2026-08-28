// Copyright (c) 2026, faris and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Library Member", {
// 	refresh(frm) {

// 	},
// });
// frappe.ui.form.on('Library Member', {
//  refresh: function(frm) {
//  frm.add_custom_button('Create Membership', () => {
//  frappe.new_doc('Library Membership', {
//  library_member: frm.doc.name
//  })
//  })
//  frm.add_custom_button('Create Transaction', () => {
//  frappe.new_doc('Library Transaction', {
//  library_member: frm.doc.name
//  })
//  })
//  }
// });

//FORM EVENTS API

// frappe.ui.form.on('Library Member',{
//     refresh(frm){
//         frm.add_custom_button('Say Hello',() => {
//             frappe.msgprint("Welcome to Library Member Form View");
//         });
//         // frm.remove_custom_button('Say Hello')
//     }
// });

// frappe.ui.form.on('Library Member',{
//     refresh(frm){
//         if (frm.is_new()){
//             frm.add_custom_button('Say Hello!!',() => {
//                 frappe.msgprint("Welcome to Library Member Form View");
//             });
//         }
//     }
// });

// frappe.ui.form.on('Library Member', {
//     refresh(frm) {

//         frm.add_custom_button('Button 1', () => {
//             frappe.msgprint('Button 1');
//         });

//         frm.add_custom_button('Button 2', () => {
//             frappe.msgprint('Button 2');
//         });

//         frm.add_custom_button('Button 3', () => {
//             frappe.msgprint('Button 3');
//         });

//         frm.clear_custom_buttons();

//     }
// });


// frappe.ui.form.on('Library Member',{
//     refresh(frm){
//         frm.set_df_property('email_address','reqd',1);
//         frm.set_df_property('phone','read_only',1);
//     }
// });


// frappe.ui.form.on('Library Member',{
//     refresh(frm){
//         frm.toggle_enable('email_address',frm.doc.check=='Active');
//     }
// });

// frappe.ui.form.on('Library Member',{
//     refresh(frm){
//         frm.toggle_reqd('email_address',frm.doc.check=='Active');
//     }
// });

// frappe.ui.form.on('Library Member',{
//     refresh(frm){
//         frm.toggle_display('email_address',frm.doc.check=='Active');
//     }
// });

// frappe.ui.form.on('Library Member', {
//     refresh(frm) {
//         frm.add_custom_button('Add Address', () => {

//             let row = frm.add_child('address', {
//                 address_line: '123 Main Street',
//                 city: 'Coimbatore',
//                 state: 'Tamil Nadu',
//                 pincode: '641001'
//             });

//             frm.refresh_field('address');

//             console.log('New address row:', row);
//         });
//     }
// });

// frappe.ui.form.on('Library Member', {
//     refresh(frm) {
//         frm.add_custom_button('Check Address Count', () => {
//             frm.call('get_address_count')
//                 .then(r => {
//                     console.log(r);
//                     frappe.msgprint(
//                         `This member has ${r.message} address row(s).`
//                     );
//                 });
//         });
//     }
// });


frappe.ui.form.on("Library Member", {
    refresh(frm) {
        frm.add_custom_button("Create Task", () => {
            let dialog = new frappe.ui.Dialog({
                title: "Create Task",
                fields: [
                    {
                        label: "Task Subject",
                        fieldname: "task_subject",
                        fieldtype: "Data",
                        reqd: 1
                    }
                ],
                primary_action_label: "Create Task",
                primary_action(values) {
                    frappe.call({
                        method: "library_management.api.create_task",
                        args: {
                            task_subject: values.task_subject
                        },
                        callback: function(r) {
                            dialog.hide();
                            frappe.msgprint({
                                title: "Success",
                                message: `Task ${r.message} created successfully.`,
                                indicator: "green"
                            });
                        }
                    });
                }
            });
            dialog.show();
        });
    }
});
