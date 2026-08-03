console.log("Library Member List Loaded");

frappe.listview_settings["Library Member"] = {
    onload(listview) {

        frappe.show_alert({
            message: "Library Member List",
            indicator: "green"
        });

        listview.page.add_inner_button("Say Hello", function () {
            frappe.msgprint("Hello from List JS");
        });

    }
};