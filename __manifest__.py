{
    'name': 'Account Cumulative Balance',
    'version': '1.0',
    'license': 'AGPL-3',
    'author': "Bilal Bayram",
    'category': 'Accounting',
    'summary': 'Show cumulative balance per account in Journal Items',
    'depends': ['account'],
    'data': [
        'views/account_move_line_views.xml',
    ],
    'installable': True,
    'application': False,
}