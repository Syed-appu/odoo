# -*- coding: utf-8 -*-
# from odoo import http


# class BankTransaction(http.Controller):
#     @http.route('/bank_transaction/bank_transaction', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bank_transaction/bank_transaction/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bank_transaction.listing', {
#             'root': '/bank_transaction/bank_transaction',
#             'objects': http.request.env['bank_transaction.bank_transaction'].search([]),
#         })

#     @http.route('/bank_transaction/bank_transaction/objects/<model("bank_transaction.bank_transaction"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bank_transaction.object', {
#             'object': obj
#         })

