from odoo import fields,models,api

class StockBatch(models.Model):
   _name = "stock.picking.batch"
   _inherit = ["stock.picking.batch"]

   dock_id = fields.Many2one('tms.dock',string='Dock')
   vehicle_id = fields.Many2one('fleet.vehicle.odometer','Vehicle')
   vehicle_category_id = fields.Many2one('fleet.vehicle.model.category','Category')
   product_weight = fields.Float(string=' Product Weight')
   product_volume = fields.Float(string='Product Volume')
   max_weight = fields.Float(compute='_compute_total_weight',string='Weight')
   max_volume = fields.Float(compute='_compute_total_weight',string='Volume')

   @api.depends('max_volume','max_weight')
   def _compute_total_weight(self):
      for record in self:
         for product in record.move_line_ids:
            record.product_weight = product.product_id.weight * product.quantity
            record.product_volume = product.product_id.volume * product.quantity

      self.max_weight = self.product_weight / self.vehicle_category_id.max_weight if self.vehicle_category_id.max_weight != 0 else 1
      self.max_volume = self.product_volume / self.vehicle_category_id.max_volume if self.vehicle_category_id.max_volume != 0 else 1

