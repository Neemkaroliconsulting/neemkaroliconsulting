from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    packaging_line_ids = fields.One2many(
        'product.packaging.line', 'product_tmpl_id', string='Packaging Lines'
    )
