frappe.ui.form.on("ToDo", {
    refresh: function(frm) {
        console.log("🔥 CUSTOM REFRESH IS RUNNING");

        frm.add_custom_button("MY CUSTOM BUTTON", function() {
            frappe.msgprint("Custom button clicked!");
        });
    },

    onload: function(frm) {
        console.log("🔥 CUSTOM ONLOAD IS RUNNING");
    }
});