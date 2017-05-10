# -*- coding: utf-8 -*-
# (Copyright) 2017 Esther Martín - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html


def update_move_line_notes(cr):
    cr.execute("""UPDATE account_move_line
                SET note = (
                    SELECT narration
                    FROM account_move
                    WHERE account_move.id = account_move_line.move_id
                );""")


def migrate(cr, version):
    if not version:
        return
    update_move_line_notes(cr)
