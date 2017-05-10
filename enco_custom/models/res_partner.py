# -*- coding: utf-8 -*-
# (Copyright) 2017 Esther Martín - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import _, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    type = fields.Selection(
        selection_add=[('shipping_material', _('Shipping material')),
                       ('online_invoice', _('Online invoice'))])
