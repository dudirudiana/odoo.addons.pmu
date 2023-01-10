from odoo import fields, api, SUPERUSER_ID, tools, modules, models

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    remark = fields.Char(string="Remark")