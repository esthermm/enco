# -*- coding: utf-8 -*-
# (c) 2016 Esther Martín - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openupgradelib import openupgrade


column_renames = {
    'purchase_order': [
        ('categ_id', None),  # many2one -> many2many
    ],
    'account_invoice': [
        ('categ_id', None),  # many2one -> many2many
    ],
}


@openupgrade.migrate()
def migrate(cr, version):
    openupgrade.rename_columns(cr, column_renames)
