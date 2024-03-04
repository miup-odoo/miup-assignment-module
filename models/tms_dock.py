from odoo import fields,models

class Dock(models.Model):
    _name = 'tms.dock'
    _description = 'Dock'

    name = fields.Char('Dock')
