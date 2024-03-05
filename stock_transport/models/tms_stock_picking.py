from odoo import fields,models,api

class StockLineMove(models.Model):
    _name = 'stock.picking'
    _inherit = ['stock.picking']
    
    volume = fields.Float('Volume',compute ="_compute_volume")
    
    @api.depends('volume')
    def _compute_volume(self):
        for record in self:
            record.volume = record.product_id.volume
