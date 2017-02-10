# -*- coding: utf-8 -*-
# © 2016 Esther Martín - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html


from openerp import fields, models


class SaleReport(models.Model):
    _inherit = 'sale.report'

    period_ack = fields.Char('ACK period', readonly=True)

    def _select(self):
        return super(SaleReport, self)._select() + \
            ", s.period_ack as period_ack"

    def _group_by(self):
        return super(SaleReport, self)._group_by() + ", s.period_ack"
