# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class unwritable_sale_discount(models.Model):
#     _name = 'unwritable_sale_discount.unwritable_sale_discount'
#     _description = 'unwritable_sale_discount.unwritable_sale_discount'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
