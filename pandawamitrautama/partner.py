from odoo import fields, api, SUPERUSER_ID, tools, modules, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_user = fields.Boolean(string="Is User", default=False)
    is_supplier = fields.Boolean(string="Is Supplier", default=False)