# -*- coding: utf-8 -*-
# (c) 2016 Ainara Galdona - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import models, fields


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    categ_ids = fields.Many2many(
        comodel_name='crm.case.categ', relation='invoice_category_rel',
        column1='order_id', column2='category_id', string='Tags',
        domain="[('object_id.model', '=', 'crm.lead')]",
        context="{'object_name': 'crm.lead'}")
    sale_ids = fields.Many2many(
        comodel_name='sale.order', relation='sale_order_invoice_rel',
        column1='invoice_id', column2='order_id', string='Sales')
    purchase_ids = fields.Many2many(
        comodel_name='purchase.order', relation='purchase_invoice_rel',
        column1='invoice_id', column2='purchase_id', string='Purchases')
