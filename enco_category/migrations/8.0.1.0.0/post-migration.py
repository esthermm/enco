# -*- coding: utf-8 -*-
# (c) 2016 Esther Martín - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import pooler
from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(cr, version):
    pool = pooler.get_pool(cr.dbname)
    # Migrate m2o categ_id to m2m categ_ids
    openupgrade.m2o_to_m2m(
        cr, pool.get('purchase.order'), 'purchase_order', 'categ_ids',
        openupgrade.get_legacy_name('categ_id'))
    openupgrade.m2o_to_m2m(
        cr, pool.get('account.invoice'), 'account_invoice', 'categ_ids',
        openupgrade.get_legacy_name('categ_id'))
