# -*- coding: utf-8 -*-
# (c) 2016 Ainara Galdona - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    @api.depends('categ_ids')
    def _compute_category_id(self):
        for record in self:
            record.category_id = record.categ_ids[:1]

    category_id = fields.Many2one(
        comodel_name='crm.case.categ',
        compute='_compute_category_id', store=True)

    @api.model
    def _make_invoice(self, order, lines):
        inv_id = super(SaleOrder, self)._make_invoice(order, lines)
        invoice = self.env['account.invoice'].browse(inv_id)
        invoice.categ_ids = [
            (6, 0, [categ_id.id for categ_id in order.categ_ids])]
        return inv_id
