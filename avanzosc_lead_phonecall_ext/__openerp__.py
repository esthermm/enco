# -*- coding: utf-8 -*-
# (c) AvanzOSC
# © 2016 Esther Martín - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Avanzosc Lead Phonecall Ext",
    "version": "8.0.1.0.0",
    "license": "AGPL-3",
    "depends": [
        "crm",
    ],
    "author": "Avanzosc",
    "category": "Custom Modules",
    "description": """
        When creating a phone call from initiatives, passed from the
        initiative the company name, contact name, and the phone call.
    """,
    "data": [
        "views/crm_phonecall_view.xml",
    ],
    "installable": True,
}
