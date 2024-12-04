from odoo import models, fields, api

class ProductPriceVariation(models.Model):
    _inherit = "product.template"

    variation_price = fields.Float(string="Variation price (%)")
    interval_start = fields.Date(string="Start date")
    interval_end = fields.Date(string="End date")
    specific_days = fields.Many2many('custom.weekday', string="Specific days")

    @api.depends('variation_price', 'interval_start', 'interval_end', 'specific_days')
    def _compute_standard_price(self):
        """
        Method to calculate the final price
        """
        for product in self:
            if product.is_variation_applicable():
                # Si la variation est applicable, appliquer le prix de la variation
                price_after_variation = (product.list_price * product.variation_price)/100
                product.standard_price = product.list_price - price_after_variation
            else:
                # Sinon, utiliser le prix standard
                product.list_price = product.standard_price

    def is_variation_applicable(self):

        #Verification if the variation is applicable today 
        today = fields.Date.today()
        current_weekday = today.strftime("%A").lower()

        for product in self : 
            #verification de jours specifiques
            applicable_days = product.specific_days.mapped('day_code')
            is_specific_day = current_weekday in applicable_days

            #conditions
            in_interval = product.interval_start and  product.interval_end and product.interval_start <= product.interval_end

            if (in_interval and is_specific_day) or (not product.interval_start and not product.interval_end and is_specific_day) or (in_interval and not applicable_days):
                return True
        
        return False 