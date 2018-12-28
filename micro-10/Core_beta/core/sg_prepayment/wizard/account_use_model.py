from odoo import fields, models, api, _
from odoo.tools.translate import _
from odoo.exceptions import ValidationError

class account_use_model(models.TransientModel):
    _name = 'account.use.model'
    _description = 'Use model'

    model = fields.Many2many('account.model', 'account_use_model_relation', 'account_id', 'model_id', string='Account Model')

    @api.model
    def view_init(self,fields_list):
        account_model_obj = self.env['account.model']
        ctx = self._context if self._context else {}
        if 'active_ids' in ctx:
            data_model = account_model_obj.browse(ctx['active_ids'])
            for model in data_model:
                for line in model.lines_id:
                    if line.date_maturity == 'partner':
                        if not line.partner_id:
                            raise ValidationError(_('Error!\n Maturity date of entry line generated by model line '+ str(line.name)+ ' is based on partner payment term!\n Please define partner on it!'))

    @api.multi
    def create_entries(self):
        account_model_obj = self.env['account.model']
        mod_obj = self.env['ir.model.data']
        ctx = self._context if self._context else {}
        data =  self.read()[0]
        record_id = ctx and ctx.get('model_line', False) or False
        if record_id:
            model_ids = data['model']
        else:
            model_ids = ctx['active_ids']
        move_ids = account_model_obj.generate(model_ids)

        context = dict(ctx, move_ids=move_ids)
        model_data_ids = mod_obj.get_object_reference('account','view_move_form')
        model_data_id = model_data_ids and model_data_ids[1] or False
        return {
            'domain': "[('id','in', ["+','.join(map(str,context['move_ids']))+"])]",
            'name': 'Entries',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'account.move',
            'views': [(False,'tree'),(model_data_id,'form')],
            'type': 'ir.actions.act_window',
        }

account_use_model()