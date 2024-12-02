import logging
from collections import defaultdict
from odoo import models, fields, api

class ProductTrending(models.Model):
    _name = 'product.trending'
    _description = 'Produits Tendance'
    _order = 'year desc, month desc, total_quantity desc'

    product_id = fields.Many2one('product.product', string='Produit', required=True)
    month = fields.Selection([
        ('jan', 'Janvier'),
        ('feb', 'Février'),
        ('mar', 'Mars'),
        ('apr', 'Avril'),
        ('may', 'Mai'),
        ('jun', 'Juin'),
        ('jul', 'Juillet'),
        ('aug', 'Août'),
        ('sep', 'Septembre'),
        ('oct', 'Octobre'),
        ('nov', 'Novembre'),
        ('dec', 'Décembre')
    ], string='Mois', required=True)
    year = fields.Integer(string='Année', required=True)
    total_quantity = fields.Float(string='Quantité Totale Vendue', required=True)
    
    @api.model
    def compute_trending_products(self):
        # Créer un logger
        logger = logging.getLogger(__name__)

        # Récupérer toutes les commandes de vente
        sales_orders = self.env['sale.order'].search([])

        # Créer un dictionnaire pour suivre les ventes de produits par mois et année
        monthly_sales = defaultdict(lambda: defaultdict(int))  # {('year', 'month'): {product_id: quantity}}

        # Parcourir toutes les commandes et les lignes de produits
        for order in sales_orders:
            # Récupérer l'année et le mois de la commande
            year_month = (order.date_order.year, order.date_order.month)  # Tuple (année, mois)

            for line in order.order_line:
                product_id = line.product_id.id
                if product_id:
                    monthly_sales[year_month][product_id] += line.product_uom_qty
                else:
                    # Log l'erreur quand le produit est NULL et continuer
                    logger.error(f"Commande {order.name} ligne {line.id} sans produit. Ignorée.")

        # Vider la table existante avant de réinjecter les données
        self.env['product.trending'].search([]).unlink()

        # Sauvegarder le produit le plus tendance (le plus vendu) pour chaque mois
        for (year, month), products in monthly_sales.items():
            # Trouver le produit avec la quantité maximale pour ce mois
            best_selling_product_id = max(products, key=products.get)
            best_selling_quantity = products[best_selling_product_id]

            # Vérifier si l'enregistrement existe déjà pour le produit, mois et année
            existing_record = self.search([
                ('year', '=', year),
                ('month', '=', self._get_month_name(month)),
                ('product_id', '=', best_selling_product_id)
            ], limit=1)

            if existing_record:
                # Mettre à jour l'enregistrement existant
                existing_record.total_quantity = best_selling_quantity
            else:
                # Créer un nouvel enregistrement pour le produit tendance
                self.create({
                    'product_id': best_selling_product_id,
                    'month': self._get_month_name(month),
                    'year': year,
                    'total_quantity': best_selling_quantity,
                })

    @staticmethod
    def _get_month_name(month_num):
        """Convertir le mois (1-12) en nom du mois."""
        month_names = {
            1: 'jan',
            2: 'feb',
            3: 'mar',
            4: 'apr',
            5: 'may',
            6: 'jun',
            7: 'jul',
            8: 'aug',
            9: 'sep',
            10: 'oct',
            11: 'nov',
            12: 'dec',
        }
        return month_names.get(month_num, 'jan')
