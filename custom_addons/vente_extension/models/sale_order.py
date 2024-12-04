from odoo import models, fields, api
import logging 
_logger = logging.getLogger(__name__)

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

            if order.has_discount:
                _logger.info(f"Order {order.id} has a discount.")
            else:
                _logger.info(f"Order {order.id} does not have a discount.")
    
    @api.onchange('order_line.discount')
    def _onchange_discount(self):   
        self._compute_has_discount()