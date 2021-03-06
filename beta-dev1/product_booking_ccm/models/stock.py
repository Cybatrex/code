# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class StockMove(models.Model):
    _inherit = 'stock.move'

    booking_order_line_id = fields.Many2one('booking.order.line',string="Booking Order Line")

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    booking_order_id = fields.Many2one('booking.order',string="Booking Order")

    @api.multi
    def write(self, vals):
        user_obj = self.env['res.users'].browse(self._uid)
        warehouse_id = self.env['stock.warehouse'].search([
                    ('company_id', '=', user_obj.company_id.id)], limit=1)
        outgoing_type_id = self.env['stock.picking.type'].search(
                        [('warehouse_id', '=', warehouse_id[0].id),
                        ('code', '=', 'outgoing')], limit=1)
        incoming_type_id = self.env['stock.picking.type'].search(
                        [('warehouse_id', '=', warehouse_id[0].id),
                        ('code', '=', 'incoming')], limit=1)
        for obj in self:
            if obj.booking_order_id:
                if obj.state == 'done':
                    for line in obj.move_lines:
                        if line.booking_order_line_id.state in ['pending','out']:
                            if obj.picking_type_id.id == outgoing_type_id.id:
                                line.booking_order_line_id.state = 'out'
                                line.booking_order_line_id.order_id.state = 'out'
                            if obj.picking_type_id.id == incoming_type_id.id:
                                line.booking_order_line_id.state = 'returned'
                                line.booking_order_line_id.order_id.state = 'returned'
        return super(StockPicking, self).write(vals)

    @api.multi
    def action_confirm(self):
        for obj in self:
            if obj.booking_order_id:
                if obj.booking_order_id.state != 'done' and obj.booking_order_id.state == 'draft':
                    obj.booking_order_id.state = 'pending'
                for line in obj.move_lines:
                    if line.product_id and line.product_id.booking_order_line_id:
                        if line.product_id.booking_order_line_id.state == 'draft':
                            line.product_id.booking_order_line_id.state = 'pending'
        return super(StockPicking, self).action_confirm()
