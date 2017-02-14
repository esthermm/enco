# -*- coding: utf-8 -*-
# (c) 2016 Ainara Galdona - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Enco Category",
    "version": "8.0.1.0.0",
    "license": "AGPL-3",
    "depends": [
        'sale_crm',
        'purchase',
        'procurement',
        'enco_purcharce_order_ext',
        'enco_sale_order_ext',
    ],
    "author": "AvanzOSC",
    "category": "Custom Module",
    "website": "www.avanzosc.es",
    'data': [
        "views/sale_view.xml",
        "views/purchase_view.xml",
        "views/account_invoice_view.xml",
        "views/crm_lead_view.xml",
        ],
    'installable': True,
}
