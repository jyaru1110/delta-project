# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    empaque = fields.Selection(string="Empaque",selection=[('P','Plegado'),('D','Desplegado')])