# /home/syed-abdullah/Downloads/odoo/addons/bank_transaction/models/bank_transaction.py

from odoo import models, fields

class BankTransaction(models.Model):
    _name = 'bank.transaction'
    _description = 'Bank Transaction'

    name = fields.Char(string='Transaction Name', required=True)
    amount = fields.Float(string='Amount', required=True)
    date = fields.Date(string='Transaction Date', required=True)
