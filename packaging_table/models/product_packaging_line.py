from odoo import models, fields, api

class ProductPackagingLine(models.Model):
    _name = 'product.packaging.line'
    _description = 'Product Packaging Line'

    product_tmpl_id = fields.Many2one(
        'product.template', string='Product', ondelete='cascade'
    )

    packaging_length = fields.Float('Length (cm)')
    width = fields.Float('Width (cm)')
    height = fields.Float('Height (cm)')
    net_weight = fields.Float('Net Weight (kg)')
    gross_weight = fields.Float('Gross Weight (kg)')
    cbm = fields.Float('CBM (m³)', compute='_compute_cbm_cft', store=True)
    cft = fields.Float('CFT', compute='_compute_cbm_cft', store=True)

    @api.depends('length', 'width', 'height')
    def _compute_cbm_cft(self):
        for rec in self:
            if rec.length and rec.width and rec.height:
                rec.cbm = (rec.length * rec.width * rec.height) / 1000000.0
                rec.cft = rec.cbm * 35.315
            else:
                rec.cbm = 0.0
                rec.cft = 0.0
