{
    'name': 'Vente Extension',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Extension pour gérer les variations de prix, les coupons et les tendances',
    'depends': ['base', 'sale', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_trending_views.xml',
        'views/product_trending_menu.xml',
    ],
    'installable': True,
    'application': True,
}
