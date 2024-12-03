import logging
from collections import defaultdict
from odoo import models, fields, api

class CategoryTrending(models.Model):
    _name = 'category.trending'
    _description = 'Tendances des Catégories de Produits'
    _order = 'year desc, month desc, total_quantity desc'

    category_id = fields.Many2one('product.category', string='Catégorie', required=True)
    month = fields.Selection([
        ('jan', 'Janvier'), ('feb', 'Février'), ('mar', 'Mars'), 
        ('apr', 'Avril'), ('mai', 'Mai'), ('jun', 'Juin'), 
        ('jul', 'Juillet'), ('aug', 'Août'), ('sep', 'Septembre'), 
        ('oct', 'Octobre'), ('nov', 'Novembre'), ('dec', 'Décembre')
    ], string='Mois', required=True)
    year = fields.Integer(string='Année', required=True)
    total_quantity = fields.Float(string='Quantité Totale Vendue', required=True)

    def compute_trending_categories(self):
        logger = logging.getLogger(__name__)
        sales_orders = self.env['sale.order'].search([])
        monthly_sales = defaultdict(lambda: defaultdict(int))

        for order in sales_orders:
            year_month = (order.date_order.year, order.date_order.month)
            for line in order.order_line.filtered(lambda l: l.product_id and l.product_id.categ_id):
                category_id = line.product_id.categ_id.id
                monthly_sales[year_month][category_id] += line.product_uom_qty
            missing_products = [line.id for line in order.order_line if not line.product_id or not line.product_id.categ_id]
            if missing_products:
                logger.error(f"Commande {order.name} lignes {missing_products} sans catégorie de produit. Ignorées.")

        self.search([]).unlink()

        for (year, month), categories in monthly_sales.items():
            best_selling_category_id, best_selling_quantity = max(categories.items(), key=lambda x: x[1])
            self.create({
                'category_id': best_selling_category_id,
                'month': self._get_month_name(month),
                'year': year,
                'total_quantity': best_selling_quantity,
            })

    @staticmethod
    def _get_month_name(month_num):
        return ['jan', 'feb', 'mar', 'apr', 'mai', 'jun', 
                'jul', 'aug', 'sep', 'oct', 'nov', 'dec'][month_num - 1]
