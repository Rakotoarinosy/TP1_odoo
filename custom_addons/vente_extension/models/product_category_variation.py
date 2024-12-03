from odoo import models, fields

class ProductCategoryVariation(models.Model):
    _inherit = "product.category"

    discount_percentage = fields.Float(string="Discount percentage")
    interval_start = fields.Date(string="Start date")
    interval_end = fields.Date(string="End date")
    specific_days = fields.Many2many('custom.weekday','day_code', string='Specific days')

    def apply_category_discount(self):
        #apply a discount to all the products in the category
        today = fields.Date.today()
        current_weekdays = today.strftime("%A").lower()
        

        for category in self :
            if category.interval_start <= today <= category.interval_end:
                applicable_days = category.specifc.days.mapped('day_code')
                if current_weekdays in applicable_days :
                    #application of the discount to all the products of the category
                    products = self.env['product.template'].search([
                        ('category_id','=', category.id)
                        ])
                    for product in products :
                        poduct.liste_price = product.standard_price * (1 - category.discount_percentage / 100)