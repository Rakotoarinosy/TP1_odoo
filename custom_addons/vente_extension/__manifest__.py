{
    'name': 'Vente Extension',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Extension pour gérer les variations de prix, les coupons et les tendances',
    'depends': ['base', 'sale', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/graph_views.xml',
        'views/vente_extension_actions.xml',
        'views/product_variation_views.xml', 
        'views/product_trending_views.xml',  
        'views/category_trending_views.xml',
        'views/product_trending_menu.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': True,
}
