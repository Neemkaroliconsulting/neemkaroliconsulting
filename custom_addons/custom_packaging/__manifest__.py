{
    'name': 'Custom Packaging',
    'version': '1.0',
    'summary': 'Manage product packaging details',
    'depends': ['base', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/packaging_views.xml',
    ],
    'installable': True,
    'application': False,
}
