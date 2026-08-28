frappe.pages["library-realtime-cha"].on_page_load = function (wrapper) {
    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: "Library Realtime Chart",
        single_column: true,
    });

    $(page.body).html(`
        <div style="padding: 20px;">
            <h3>Library Realtime Chart</h3>
            <div id="library-chart"></div>
        </div>
    `);

    let labels = [];
    let values = [];

    let chart = new frappe.Chart("#library-chart", {
        title: "Books Issued",
        data: {
            labels: labels,
            datasets: [{ name: "Books Issued", values: values }],
        },
        type: "line",
        height: 300,
    });

    // listen for realtime updates and manually push new points
    frappe.realtime.on("library_chart_update", function (data) {
        labels.push(data.label);
        values.push(data.points[0]);

        // keep only the last 8 labels, like max_label_count did
        if (labels.length > 8) {
            labels.shift();
            values.shift();
        }

        chart.update({
            labels: labels,
            datasets: [{ name: "Books Issued", values: values }],
        });
    });

    frappe.call({
        method: "library_management.api.send_chart_data",
    });
};