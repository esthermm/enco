# -*- coding: utf-8 -*-
# © 2017 Esther Martín - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html


from openerp import fields, models
from openerp import tools


class PurchaseReport(models.Model):
    _inherit = 'purchase.report'

    period_ack = fields.Char(string='ACK Period', readonly=True)
