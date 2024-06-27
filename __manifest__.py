# /home/syed-abdullah/Downloads/odoo/addons/bank_transaction/__manifest__.py

{
    'name': 'Bank Transactions',
    'version': '1.0',
    'summary': 'Manage bank transactions',
    'sequence': -100,
    'description': """Manage bank transactions""",
    'category': 'Accounting',
    'author': 'Your Name',
    'website': 'http://www.yourcompany.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
