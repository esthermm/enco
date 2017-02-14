# -*- coding: utf-8 -*-
# (c) 2016 Ainara Galdona - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import api, models, fields


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    categ_ids = fields.Many2many(
        comodel_name='crm.case.categ', relation='purchase_order_category_rel',
        column1='order_id', column2='category_id', string='Tags',
        domain="[('object_id.model', '=', 'crm.lead')]",
        context="{'object_name': 'crm.lead'}")

    @api.multi
    @api.depends('categ_ids')
    def _compute_category_id(self):
        for record in self:
            record.category_id = record.categ_ids[:1]

    category_id = fields.Many2one(
        comodel_name='crm.case.categ',
        compute='_compute_category_id', store=True)

    @api.multi
    def action_invoice_create(self):
        res = super(PurchaseOrder, self).action_invoice_create()
        for order in self:
            for invoice in order.invoice_ids:
                invoice.categ_ids = order.categ_ids.ids
        return res
