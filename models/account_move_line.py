from odoo import models, fields, api

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    cumulative_balance = fields.Monetary(
        string='Cumulative',
        compute='_compute_cumulative_balance',
        currency_field='currency_id',
        store=False
    )

    @api.depends('account_id', 'date', 'debit', 'credit')
    def _compute_cumulative_balance(self):
        for line in self:
            domain = [
                ('account_id', '=', line.account_id.id),
                ('date', '<=', line.date),
                ('company_id', '=', line.company_id.id),
                ('move_id.state', '=', 'posted'),
            ]
            lines = self.env['account.move.line'].search(domain, order='date ASC, id ASC')
            balance = 0
            for l in lines:
                balance += l.debit - l.credit
                if l.id == line.id:
                    break
            line.cumulative_balance = balance

