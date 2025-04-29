from odoo import models, fields, api

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    cumulative_balance = fields.Monetary(
        string='Cumulative Balance',
        compute='_compute_cumulative_balance',
        currency_field='currency_id',
        store=False
    )

    @api.depends('account_id', 'date', 'debit', 'credit')
    def _compute_cumulative_balance(self):
        for line in self:
            self.env.cr.execute("""
                SELECT SUM(debit - credit) 
                FROM account_move_line
                WHERE account_id = %s
                AND date <= %s
                AND company_id = %s
                AND move_id IN (SELECT id FROM account_move WHERE state = 'posted')
            """, (line.account_id.id, line.date, line.company_id.id))
            result = self.env.cr.fetchone()
            line.cumulative_balance = result[0] or 0.0