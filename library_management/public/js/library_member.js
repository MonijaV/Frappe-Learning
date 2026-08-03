console.log("Library Member JS Loaded!");

frappe.ui.form.on("Library Member", {
    refresh(frm) {
        frappe.show_alert({
            message: "Library Member Form Opened",
            indicator: "green"
        });

        frm.add_custom_button("Hello", function () {
            frappe.msgprint("Hello from doctype_js!");
        });
    }
});