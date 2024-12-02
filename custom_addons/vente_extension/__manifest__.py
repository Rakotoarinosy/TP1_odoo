{
    'name': 'Vente Extension',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Extension pour gérer les variations de prix, les coupons et les tendances',
    'depends': ['base', 'sale', 'product'],
    'data': [
        'views/product_trending_menu.xml',
        'views/product_trending_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
