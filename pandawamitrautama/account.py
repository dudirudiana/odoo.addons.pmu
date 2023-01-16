from odoo import fields, api, SUPERUSER_ID, tools, modules, models, _
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = 'account.move'
    _sql_constraints = [('unique_duplication_number', 'unique(duplication_number)', 'Show message here!'),]

    @api.model
    def _get_company(self):
         return self.env.user.company_id.id

    company_id = fields.Many2one('res.company', string="Company", required=True, default=_get_company)

    # def action_post(self):
    #     # raise UserError(_(str(self.name)))
    #     if self:
    #         self.name = self.env["ir.sequence"].search([('active', '=', True)]).next_by_code("account.move")