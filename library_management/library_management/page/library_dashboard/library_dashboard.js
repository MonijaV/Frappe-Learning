frappe.pages['library-dashboard'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Library Dashboard',
		single_column: true
	});
	console.log("Page object:", page);
	page.set_title("My Library Dashboard");
	// page.set_title_sub("Heloo!!");
	page.set_indicator("Pending", "orange");
	page.clear_indicator();

	page.set_primary_action("New", () => {
        console.log("New button clicked!");
    });
};