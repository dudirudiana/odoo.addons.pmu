from odoo import fields, api, SUPERUSER_ID, tools, modules, models

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model
    def create(self, vals):
        company = self.env.user.company_id
        result = super(AccountAssetAsset, self).create(vals)
        if result.category_id and result.subcategory_id and not result.code:
            asset_code = result.subcategory_id.sequence_id.next_by_id()    
            result.sequence = asset_code
            result.code = asset_code