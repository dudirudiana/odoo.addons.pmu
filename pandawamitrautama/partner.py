from odoo import fields, api, SUPERUSER_ID, tools, modules, models, _
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    npwp = fields.Char(string="NPWP")
    pic = fields.Char(string="PIC")
    code = fields.Char(string="Code")
    is_active = fields.Boolean(string="Is Active", default=True)
    is_ppn = fields.Boolean(string="Is Ppn", default=False)
    is_user = fields.Boolean(string="Is User", default=False)
    is_supplier = fields.Boolean(string="Is Supplier", default=False)
    is_customer = fields.Boolean(string="Is Customer", default=False)
    pid = fields.Char(string="Partner Id")

    @api.model
    def create(self, vals):
        # raise UserError(_(vals))
        vals['pid'] = self.env["ir.sequence"].search([('active', '=', True)]).next_by_code("res.partner")
        # raise UserError(_(str(vals['pid'])))
        result = super(ResPartner, self).create(vals)
        return result