from odoo import models, fields

class Weekdays(models.Model):
    _name= 'custom.weekday'
    _description = "Specific days for price variations"


    name = fields.Char(string="Day name", required=True)
    day_code = fields.Selection([
        ('monday','Monday'),
        ('tuesday','Tuesday'),
        ('wednesday','Wednesday'),
        ('thursday','Thursday'),
        ('friday','Friday'),
        ('saturday','Saturday'),
        ('sunday','Sunday'),
    ], string="Day code", required=True, unique=True)