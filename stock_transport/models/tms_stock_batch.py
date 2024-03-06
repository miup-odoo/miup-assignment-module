from odoo import fields,models,api

class StockBatch(models.Model):
   _inherit = ["stock.picking.batch"]

   dock_id = fields.Many2one('tms.dock',string='Dock')
   vehicle_id = fields.Many2one('fleet.vehicle','Vehicle')
   vehicle_category_id = fields.Many2one('fleet.vehicle.model.category','Category')
   product_weight = fields.Float(string='Weight',compute='_compute_total_weight',store=True)
   product_volume = fields.Float(string='Volume', compute='_compute_total_volume',store=True)
   max_weight = fields.Float(string='Max Weight',compute='_compute_total_weight_percentage')
   max_volume = fields.Float(string='Max Volume',compute='_compute_total_volume_percentage')
   transfer = fields.Integer(string='Transfer',compute="_compute_total_transfer",store=True)
   line = fields.Integer(string="Line",compute="_compute_total_line",store=True)

   @api.depends('picking_ids.move_ids.product_id.volume','picking_ids.move_ids.quantity','product_volume')
   def _compute_total_volume(self):
      for record in self:
         record.product_volume = 0
         for transfer in record.picking_ids:
            for product in transfer.move_ids:
               record.product_volume += product.product_id.volume * product.quantity
               

   @api.depends('picking_ids.move_ids.product_id.weight','picking_ids.move_ids.quantity','product_weight')
   def _compute_total_weight(self):
      for record in self:
         record.product_weight = 0
         for transfer in record.picking_ids:
            for product in transfer.move_ids:
               record.product_weight += product.product_id.weight * product.quantity  
                       

   @api.depends('product_volume')
   def _compute_total_volume_percentage(self):
      for record in self:
         record.max_volume = (100 * record.product_volume) / record.vehicle_category_id.max_volume if record.vehicle_category_id.max_volume != 0 else 0
   
   @api.depends('product_weight')
   def _compute_total_weight_percentage(self):
      for record in self:
         record.max_weight = (100 * record.product_weight) / record.vehicle_category_id.max_weight if record.vehicle_category_id.max_weight != 0 else 0
        
   def _compute_display_name(self):
        for record in self:
            name = record.name
            if name:
                name = f"{record.name}: {record.max_weight}kg, {record.max_volume}m\xb3"
            record.display_name = name

   @api.depends('picking_ids')
   def _compute_total_transfer(self):
      for record in self:
         record.transfer = len(record.picking_ids)
      
   @api.depends('move_ids')
   def _compute_total_line(self):
      for record in self:
         record.line = len(record.move_ids)
