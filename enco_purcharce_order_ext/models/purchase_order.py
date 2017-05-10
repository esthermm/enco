# -*- coding: utf-8 -*-
# (c) Manuel Guil
# © 2016 Esther Martín - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import models, fields
from openerp.exceptions import except_orm, Warning, RedirectWarning




class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    period_ack = fields.Char('ACK Period', size=6, required=True)
    client_id  = fields.Char('Client', size=60, required=True)
    
    #------

    def do_merge(self, cr, uid, ids, context=None):
        #------
        order_infos = super(PurchaseOrder, self).do_merge( cr, uid, ids, context)
        
        new_po = self.pool.get('purchase.order')._get_purchase_order(cr, uid, order_infos, context)
        #old_po = self.pool.get('purchase.order')._get_purchase_order(cr, uid, ids[0], context)
        old_order = self.browse(cr, uid, ids[0], context=context)
        #---
        self.write(cr, uid, new_po, {'period_ack': old_order.period_ack}, context=context)
        self.write(cr, uid, new_po, {'client_id':  old_order.client_id}, context=context)
        self.write(cr, uid, new_po, {'categ_ids':  [(6, 0, [old_order.categ_ids.ids])]}, context=context)
        #--
        #raise Warning("Error5!", (ids, new_po)  )

        return order_infos
