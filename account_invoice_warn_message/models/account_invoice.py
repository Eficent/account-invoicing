# Copyright 2020 ForgeFlow S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    invoice_warn_msg = fields.Text(compute="_compute_invoice_warn_msg")

    @api.depends('type', 'state',
                 'partner_id.commercial_partner_id.invoice_warn')
    def _compute_invoice_warn_msg(self):
        for rec in self:
            p = rec.partner_id.commercial_partner_id
            if (
                rec.type in ("out_invoice", "out_refund")
                and rec.state == "draft"
                and p.invoice_warn == "warning"
            ):
                rec.invoice_warn_msg = p.invoice_warn_msg
                continue
            rec.invoice_warn_msg = False
