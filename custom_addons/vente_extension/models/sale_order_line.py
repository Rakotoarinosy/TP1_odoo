from odoo import mmodesl, fields, api 

class SaleOrderLine(self):
    _inherit = 'sale.order.line'

    @api.onchange('product_id')
    def _apply_discount_by_variation(self):
        #Apply discount if variation_price conditions is True

        for line in self:
            product = line.product_id.product_tmpl_id
            if product.is-variation_applicable():
                line.discount= 100 - ((product.variaiton_price / line.price_unit)*100)
            else : 
                line.discount = 0


    @api.onchange('product_id')
    def _apply_category_discount(self):
        """
        Applique la remise de la catégorie à la ligne de commande si applicable.
        """
        for line in self:
            product = line.product_id.product_tmpl_id
            category = product.categ_id

            # Vérifier si la catégorie a une remise applicable
            if category.is_category_discount_applicable():
                line.discount = category.discount_percentage
            else:
                line.discount = 0
