# -*- coding: utf-8 -*-
# (c) 2016 Ainara Galdona - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import api, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def _prepare_invoice(self, order, lines):
        vals = super(SaleOrder, self)._prepare_invoice(order, lines)
        vals['categ_ids'] = [(6, 0, order.categ_ids.ids)]
        return vals
