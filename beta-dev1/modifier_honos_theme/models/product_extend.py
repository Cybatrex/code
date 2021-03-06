import odoo
import logging
from odoo import fields, models, api, _
from odoo.http import request
from odoo.exceptions import UserError, ValidationError
import math
import werkzeug
_logger = logging.getLogger(__name__)

class featured_products(models.Model):
    _name = 'featured.products'
    _description = "Info Featured Products"
    
    name= fields.Char('Name', required=True)
    featured_products_line_ids = fields.One2many('featured.products.line', 'featured_products_id', string='Featured Products Line')


class featured_products_line(models.Model):
    _name = 'featured.products.line'
    _description = "Info of Featured Products Lines"
    
    featured_products_id = fields.Many2one('featured.products', string='Featured Products', ondelete='cascade')#O2M
    name = fields.Integer('Sequence')
    products_id = fields.Many2one('product.product', required=True, string='Product')


class new_arrival(models.Model):
    _name = 'new.arrival'
    _description = "Info of New Arrivals"
    
    name= fields.Char('Name', required=True)
    new_arrival_products_line_ids = fields.One2many('new.arrival.line', 'new_arrival_products_id', string='New Arrival Products Line')


class new_arrival_line(models.Model):
    _name = 'new.arrival.line'
    _description = "Info of New Arrivals Products Lines"
    
    new_arrival_products_id = fields.Many2one('new.arrival', string='New Arrivals', ondelete='cascade')#O2M
    name = fields.Integer('Sequence')
    products_id = fields.Many2one('product.product', required=True, string='Product')
