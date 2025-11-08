from odoo import models, fields, api

class ProductPackagingLine(models.Model):
    _name = 'product.packaging.line'
    _description = 'Product Packaging Line'

    product_tmpl_id = fields.Many2one('product.template', string='Product', ondelete='cascade')
    item_level = fields.Selection([
        ('l1', 'L1 - Poly Pack'),
        ('l2', 'L2 - Inner Box'),
        ('l3', 'L3 - Master Carton'),
        ('l4', 'L4 - Outer Carton'),
    ], string='Item Level')
    length = fields.Float('Length (cm)')
    width = fields.Float('Width (cm)')
    height = fields.Float('Height (cm)')
    net_weight = fields.Float('Net Wt (kg)')
    gross_weight = fields.Float('Gross Wt (kg)')
    cbm = fields.Float('CBM (m³)', compute='_compute_cbm', store=True)
    cft = fields.Float('CFT', compute='_compute_cft', store=True)

    @api.depends('length', 'width', 'height')
    def _compute_cbm(self):
        for rec in self:
            rec.cbm = (rec.length * rec.width * rec.height) / 1000000.0 if rec.length and rec.width and rec.height else 0.0

    @api.depends('cbm')
    def _compute_cft(self):
        for rec in self:
            rec.cft = rec.cbm * 35.315 if rec.cbm else 0.0
