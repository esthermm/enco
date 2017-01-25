# -*- coding: utf-8 -*-
# © 2017 Ainara Galdona - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import models
from openerp.addons.account.report.account_general_ledger import general_ledger


class report_enco_generalledger(models.AbstractModel):
    _name = 'report.enco_general_ledger.report_enco_generalledger'
    _inherit = 'report.abstract_report'
    _template = 'enco_general_ledger.report_enco_generalledger'
    _wrapped_report_class = general_ledger
