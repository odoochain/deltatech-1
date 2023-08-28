# ©  2008-2021 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details
{
    "name": "eCommerce Category Snippet",
    "category": "Website",
    "summary": "eCommerce extension Category Snipped",
    "version": "15.0.1.0.1",
    "author": "Terrabit, Dorin Hongu",
    "license": "OPL-1",
    "website": "https://www.terrabit.ro",
    "depends": ["website_sale", "deltatech_website_category"],
    "data": ["views/templates.xml", "views/snippets.xml"],
    "images": ["static/description/main_screenshot.png"],
    "installable": True,
    "qweb": ["static/src/xml/*.xml"],
    "development_status": "Alpha",
    "maintainers": ["dhongu"],
    "assets": {
        "web.assets_frontend": [
            "deltatech_website_category_snippet/static/src/js/website_category_card.js",
            "deltatech_website_category_snippet/static/src/scss/s_category_card.scss",
        ],
        "website.assets_editor": ["/deltatech_website_category_snippet/static/src/js/website_category_card_editor.js"],
    },
}
