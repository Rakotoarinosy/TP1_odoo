from odoo import models, fields

class ProductPriceVariation(models.Model):
    _inherit = "product.template"

    variation_price = fields.Float(string="Variation price")
    interval_start = fields.Date(string="Start date")
    interval_end = fields.Date(string="End date")
    specific_days = fields.Many2many('custom.weekday', string="Specific days")

    def _compute_price(self):
        #Method to calculate the price by the variation
        today = fields.Date.today()
        current_weekday = today.strftime("%A").lower()

        for product in self:
            if product.interval_start <= today <= product.interval_end: 
                applicable_days = product.specific_days.mapped('day_code')
                if current_weekday in applicable_keys:
                    product.list_price = product.variation_price
                else:
                    product.list_price = product.standard_price
            else:
                product.list_price = product.standard_price