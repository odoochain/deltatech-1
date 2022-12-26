# ©  2008-2021 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details


from odoo import fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    l10n_ro_notice = fields.Boolean()

    def action_view_sale_invoice(self):
        if self.sale_id:
            action = self.env["ir.actions.actions"]._for_xml_id("sale.action_view_sale_advance_payment_inv")
            action["context"] = {"active_id": self.sale_id.id, "active_ids": self.sale_id.ids, "l10n_ro_notice": True}
            return action
