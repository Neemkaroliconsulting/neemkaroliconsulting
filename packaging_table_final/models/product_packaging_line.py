from odoo import models, fields, api

class ProductPackagingLine(models.Model):
    _name = 'product.packaging.line'
    _description = 'Product Packaging Line'

    product_tmpl_id = fields.Many2one('product.template', string='Product', ondelete='cascade')

    # length_cm = fields.Float('Length (cm)')
    width_cm = fields.Float('Width (cm)')
    height_cm = fields.Float('Height (cm)')
    net_weight = fields.Float('Net Weight (kg)')
    gross_weight = fields.Float('Gross Weight (kg)')
    cbm = fields.Float('CBM (m³)', compute='_compute_cbm', store=True)
    cft = fields.Float('CFT', compute='_compute_cbm', store=True)

    @api.depends('length_cm', 'width_cm', 'height_cm')
    def _compute_cbm(self):
        for rec in self:
            if rec.width_cm and rec.height_cm:
                rec.cbm = (rec.width_cm * rec.height_cm) / 1000000
                rec.cft = rec.cbm * 35.315
            else:
                rec.cbm = 0.0
                rec.cft = 0.0
