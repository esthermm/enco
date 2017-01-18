# -*- coding: utf-8 -*-
# © 2016 Esther Martín - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Enco Analytic Menu",
    "version": "8.0.1.0.0",
    "author": "AvanzOSC",
    "license": "AGPL-3",
    "category": "Custom module",
    "website": "http://www.avanzosc.es",
    "contributors": [
        "Ana Juaristi <ajuaristio@gmail.com>",
        "Esther Martín <esthermartin@avanzosc.es>",
    ],
    "depends": [
        "analytic",
        "sale",
        ],
    "data": [
        "views/analytic_security.xml",
        "views/analytic_view.xml",
        "views/sale_view.xml",
        "security/ir.model.access.csv",
        ],
    "installable": True
}
