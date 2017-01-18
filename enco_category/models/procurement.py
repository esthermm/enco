# -*- coding: utf-8 -*-
# (c) 2016 Ainara Galdona - AvanzOSC
# (c) 2016 Esther Martín - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import api, models


class ProcurementOrder(models.Model):
    _inherit = 'procurement.order'

    @api.model
    def create_procurement_purchase_order(self, procurement, po_vals,
                                          line_vals):
        sale = procurement.group_id.mapped(
            'procurement_ids.sale_line_id.order_id')
        po_vals['categ_ids'] = [(6, 0, sale.categ_ids.ids)]
        return super(ProcurementOrder, self).create_procurement_purchase_order(
            procurement, po_vals, line_vals)
