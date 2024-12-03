from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    has_discount = fields.Boolean(
        string = "Has discount",
        compute = "_compute_has_discount",
        store = True
    )


    def _compute_has_discount(self):
        for order in self:
            #check if the line has a discount
            order.has_discount = any(line.discount > 0 for line in order.order_line)
