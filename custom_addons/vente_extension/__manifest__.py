{
    'name': 'Vente Extension',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Extension pour gérer les variations de prix, les coupons et les tendances',
    'depends': ['base', 'sale', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/vente_extension_actions.xml',
        'views/product_variation_views.xml',
        'views/category_variation_views.xml',        
    ],
    'installable': True,
    'application': True,
}
