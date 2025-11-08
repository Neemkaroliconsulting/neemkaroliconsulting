from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    packaging_type = fields.Selection([
        ('box', 'Box'),
        ('bag', 'Bag'),
        ('roll', 'Roll'),
    ], string="Packaging Type")

    packaging_weight = fields.Float(string="Packaging Weight (kg)")
