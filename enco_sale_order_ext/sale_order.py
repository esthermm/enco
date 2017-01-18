# -*- coding: utf-8 -*-
# © 2016 Esther Martín - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    period_ack = fields.Char(string='ACK Period', size=6)
