from odoo import models,fields,api

class StockTransport(models.Model):
    _name = 'fleet.vehicle.model.category'
    _inherit=['fleet.vehicle.model.category']

    max_weight = fields.Float('Max Weight(kg)')
    max_volume = fields.Float('Max Volume(m^3)')

    @api.depends('max_weight','max_volume')
    def _compute_display_name(self):
        for record in self:
            name = record.name
            if name:
                name = f"{record.name}({record.max_weight}kg, {record.max_volume}m^3)"
            record.display_name = name
