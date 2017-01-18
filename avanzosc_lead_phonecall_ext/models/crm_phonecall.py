# -*- coding: utf-8 -*-
# (c) AvanzOSC
# © 2016 Esther Martín - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import models, fields


class CrmPhonecall(models.Model):
    _inherit = 'crm.phonecall'

    contact_name = fields.Char('Contact Name', size=64)
    partner_name = fields.Char(
        "Customer Name", size=64,
        help='The name of the future partner that will be created while '
        'converting the lead into opportunity', select=1)
