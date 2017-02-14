# -*- coding: utf-8 -*-
# © 2016 Esther Martín - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html


from openerp import fields, models


class SaleReport(models.Model):
    _inherit = 'sale.report'

    category_id = fields.Many2one(comodel_name='crm.case.categ', readonly=True)

    def _select(self):
        return super(SaleReport, self)._select() + \
            ", s.category_id as category_id"

    def _group_by(self):
        return super(SaleReport, self)._group_by() + ", s.category_id"
