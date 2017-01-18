# -*- coding: utf-8 -*-
# (c) Manuel Guil
# © 2016 Esther Martín - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import models, fields


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    period_ack = fields.Char('ACK Period', size=6)
