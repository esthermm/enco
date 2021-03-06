# -*- coding: utf-8 -*-
# (Copyright) 2017 Esther Martín - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    note = fields.Text()
    received_check = fields.Boolean(string='Received check',
        help="To write down that a check in paper support has been received, "
        "for example.")
