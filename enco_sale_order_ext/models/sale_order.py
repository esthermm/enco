# -*- coding: utf-8 -*-
# (c) Manuel Guil
# © 2016 Esther Martín - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    period_ack = fields.Char(string='ACK Period', size=6, required=True)
    
    
    #@api.one
    def action_button_confirm(self, cr, uid, ids, context=None):  
        return super(SaleOrder, self).action_button_confirm(cr, uid, ids, context)
