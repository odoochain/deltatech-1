# ©  2008-2022 Deltatech
# See README.rst file on addons root folder for license details

{
    "name": "Logistic Documents",
    "summary": "Logistic Documents",
    "version": "15.0.1.0.3",
    "author": "Terrabit, Dorin Hongu",
    "website": "https://www.terrabit.ro",
    "license": "OPL-1",
    "category": "Generic Modules",
    "depends": ["purchase_stock", "sale_stock"],
    "data": [
        "views/stock_picking_view.xml",
        "views/sale_order_view.xml",
        "views/purchase_order_view.xml",
        "views/account_invoice_view.xml",
        "views/ir_attachment_view.xml",
    ],
    "images": ["static/description/main_screenshot.png"],
    "development_status": "Beta",
}
