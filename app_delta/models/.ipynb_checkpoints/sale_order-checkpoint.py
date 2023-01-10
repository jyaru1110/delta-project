# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    empaque = fields.Selection(string="Empaque",selection=[('P','Plegado'),('D','Desplegado')])
    folio_vendedor = fields.Text(string="Folio por vendedor")
    
    @api.model_create_multi
    def create(self,values):
        num_folios = len(self.env['sale.order'].search_read([('user_id','=',values['user_id'])],['id']))
        values['folio_vendedor'] = self.env['res.users'].search_read([('user_id','=',values['user_id'])],['prefijo']) + str(num_folios)
        override_create = super(SaleOrder,self).create(values)
        return override_create