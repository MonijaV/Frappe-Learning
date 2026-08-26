// Copyright (c) 2026, faris and contributors
// For license information, please see license.txt

// frappe.treeview_settings["Library Category"] = {
// };


// frappe.treeview_settings["Library Category"] = {
//     breadcrumb: "Library Management",
//     title: "Library Categories"
// };

// frappe.treeview_settings["Library Category"] = {
//     breadcrumb: "Library Management",
//     title: "Library Categories",
//     filters: [
//         {
//             fieldname: "category_type",
//             fieldtype: "Select",
//             label: "Category Type",
//             options: "Books\nHello\nFiction"
//         }
//     ]
// };

// frappe.treeview_settings["Library Category"] = {
//     breadcrumb: "Library Management",
//     title: __("Library Category Tree"),

//     get_tree_nodes: "frappe.desk.treeview.get_children",
//     add_tree_node: "frappe.desk.treeview.add_node",

//     fields: [
//         {
//             fieldtype: "Data",
//             fieldname: "category_name",
//             label: __("Category Name"),
//             reqd: true,
//         },
//         {
//             fieldtype: "Check",
//             fieldname: "is_group",
//             label: __("Is Group"),
//         },
//     ],

//     ignore_fields: ["parent_library_category"],

//     extend_toolbar: true,

//     toolbar: [
//         {
//             label: __("Add Child"),
//             condition: function (node) {
//                 return node && node.is_group;
//             },
//             click: function (node) {
//                 frappe.treeview_settings["Library Category"].add_node(node);
//             },
//             btnClass: "hidden-xs",
//         },
//     ],

//     menu_items: [
//         {
//             label: __("New Library Category"),
//             action: function () {
//                 frappe.new_doc("Library Category", true);
//             },
//             condition: "frappe.boot.user.can_create.indexOf('Library Category') !== -1",
//         },
//     ],

//     onload: function (treeview) {
//         console.log("Tree loaded");
//     },

//     post_render: function (treeview) {
//         console.log("Whole tree rendered");
//     },

//     onrender: function (node) {
//         console.log("Node rendered:", node);
//     },

//     on_get_node: function (nodes) {
//         console.log("Nodes received:", nodes);
//     },
// };