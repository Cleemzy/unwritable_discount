# -*- coding: utf-8 -*-
# from odoo import http


# class UnwritableSaleDiscount(http.Controller):
#     @http.route('/unwritable_sale_discount/unwritable_sale_discount/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/unwritable_sale_discount/unwritable_sale_discount/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('unwritable_sale_discount.listing', {
#             'root': '/unwritable_sale_discount/unwritable_sale_discount',
#             'objects': http.request.env['unwritable_sale_discount.unwritable_sale_discount'].search([]),
#         })

#     @http.route('/unwritable_sale_discount/unwritable_sale_discount/objects/<model("unwritable_sale_discount.unwritable_sale_discount"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('unwritable_sale_discount.object', {
#             'object': obj
#         })
