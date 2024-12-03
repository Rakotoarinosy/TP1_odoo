from collections import defaultdict
import logging
from odoo import models, fields, api

class ProductTrending(models.Model):
    _name = 'product.trending'
    _description = 'Produits Tendance'
    _order = 'year desc, month desc, total_quantity desc'

    product_id = fields.Many2one('product.product', string='Produit', required=True)
    month = fields.Selection([
        ('jan', 'Janvier'), ('feb', 'Février'), ('mar', 'Mars'), 
        ('apr', 'Avril'), ('mai', 'Mai'), ('jun', 'Juin'), 
        ('jul', 'Juillet'), ('aug', 'Août'), ('sep', 'Septembre'), 
        ('oct', 'Octobre'), ('nov', 'Novembre'), ('dec', 'Décembre')
    ], string='Mois', required=True)
    year = fields.Integer(string='Année', required=True)
    total_quantity = fields.Float(string='Quantité Totale Vendue', required=True)

    # @api.model
    def compute_trending_products(self):
        logger = logging.getLogger(__name__)
        sales_orders = self.env['sale.order'].search([])
        monthly_sales = defaultdict(lambda: defaultdict(int))

        # Collecte des ventes mensuelles
        for order in sales_orders:
            year_month = (order.date_order.year, order.date_order.month)
            for line in order.order_line.filtered(lambda l: l.product_id):
                monthly_sales[year_month][line.product_id.id] += line.product_uom_qty
            missing_products = [line.id for line in order.order_line if not line.product_id]
            if missing_products:
                logger.error(f"Commande {order.name} lignes {missing_products} sans produit. Ignorées.")

        # Supprimer les anciens enregistrements avant d'ajouter les nouveaux
        self.search([]).unlink()

        # Créer des enregistrements pour les produits tendance
        for (year, month), products in monthly_sales.items():
            best_selling_product_id, best_selling_quantity = max(products.items(), key=lambda x: x[1])
            self.create({
                'product_id': best_selling_product_id,
                'month': self._get_month_name(month),
                'year': year,
                'total_quantity': best_selling_quantity,
            })

    def display_trending_products(self):
        trending_products = self.search([])
        results = []
        for product in trending_products:
            results.append(f"{product.product_id.name} {product.year} {product.month} {product.total_quantity}")
        return "\n".join(results)

    @staticmethod
    def _get_month_name(month_num):
        return ['jan', 'feb', 'mar', 'apr', 'mai', 'jun', 
                'jul', 'aug', 'sep', 'oct', 'nov', 'dec'][month_num - 1]
