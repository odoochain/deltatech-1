# ©  2008-2021 Deltatech
# See README.rst file on addons root folder for license details
{
    "name": "Deltatech Batch Transfer",
    "summary": "Batch transfer improvements",
    "version": "15.0.0.0.2",
    "author": "Terrabit, Dan Stoica",
    "website": "https://www.terrabit.ro",
    "support": "odoo@terrabit.ro",
    "category": "Stock",
    "external_dependencies": {"python": []},
    "depends": ["stock", "stock_picking_batch", "sale_stock", "purchase_stock"],
    "data": [
        "wizard/stock_prepare_batch_view.xml",
        "security/ir.model.access.csv",
        "views/stock_picking_batch.xml",
    ],
    "license": "OPL-1",
    "development_status": "Beta",
    "images": ["static/description/main_screenshot.png"],
    "maintainers": ["danila12"],
}
