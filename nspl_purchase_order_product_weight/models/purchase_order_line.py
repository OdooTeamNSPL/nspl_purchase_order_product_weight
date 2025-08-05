from odoo import models, fields, api

class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    product_weight = fields.Float(
        string="Unit Weight",
        related="product_id.weight",
        readonly=True,
        store=True,
    )
    line_total_weight = fields.Float(
        string="Total Weight",
        compute="_compute_line_total_weight",
        store=True,
    )

    @api.depends("product_weight", "product_qty")
    def _compute_line_total_weight(self):
        for line in self:
            line.line_total_weight = line.product_weight * line.product_qty


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    total_weight = fields.Float(
        string="Total Weight",
        compute="_compute_total_weight",
        store=True,
    )

    @api.depends("order_line.line_total_weight")
    def _compute_total_weight(self):
        for order in self:
            order.total_weight = sum(order.order_line.mapped("line_total_weight"))
