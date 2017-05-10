# -*- coding: utf-8 -*-
# (c) 2016 Esther Martín - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

import datetime
from openerp import models

class ProcurementOrder(models.Model):
    _inherit = 'procurement.order'

    def create_procurement_purchase_order(self, cr, uid, procurement, po_vals, line_vals, context=None):
        sale = procurement.group_id.mapped(
            'procurement_ids.sale_line_id.order_id')
        # Actualizamos el period_ack
        now = datetime.datetime.now()
        sale.period_ack = '%sT%s' % (now.year-2000,now.month/3+1)
        #
        po_vals['period_ack'] = sale.period_ack
        po_vals['client_id'] = sale.partner_id.display_name
         
        return super(ProcurementOrder, self).create_procurement_purchase_order(cr, uid, procurement, po_vals, line_vals, context)
