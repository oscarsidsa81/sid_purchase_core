# -*- coding: utf-8 -*-
from odoo import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    # HS code del producto (delivery)
    sid_hs_code = fields.Char(
        string="Code HS",
        related="product_id.hs_code",
        store=False,
        readonly=True,
        help="z.HS Code",
    )

    # Copia almacenada del HS code para la lÃ­nea
    sid_hs_code_po_line = fields.Char(
        string="HS Code (po)",
        related="sid_hs_code",
        store=True,
        readonly=False,
        help="HS Code",
    )

    sid_invoice = fields.Selection(
        selection=[
            ("facturar", "Facturar"),
            ("abono", "Abono"),
            ("facturado", "Facturado"),
            ("pendiente", "Pendiente"),
        ],
        string="Facturacion",
        compute="_compute_sid_invoice",
        store=True,
        readonly=True,
    )

    supplier_country = fields.Many2one(
        "res.country",
        string="Pais Origen",
        related="order_id.partner_id.country_id",
        store=True,
        readonly=True,
    )

    pending_line = fields.Selection(
        selection=[
            ("true", "Si"),
            ("false", "No"),
        ],
        string="Pendiente",
        compute="_compute_pending_line",
        store=True,
        readonly=True,
    )

    sid_qty_inv_sale = fields.Float(
        string="Cantidad Facturada Venta",
        related="sale_line_id.qty_invoiced",
        store=True,
        readonly=True,
    )

    sid_sale_date = fields.Datetime(
        string="Fecha Venta",
        related="sale_line_id.calculated_date",
        store=True,
        readonly=True,
        help="Fecha Contrato Venta",
    )

    sid_unit_price_difference = fields.Monetary(
        string="Balance Venta-Compra",
        currency_field="currency_id",
        store=True,
        readonly=False,
        help="Campo legado (sin computo en la exportacion).",
    )

    sid_unit_weight_product = fields.Float(
        string="Peso unitario (producto)",
        related="product_id.weight",
        store=False,
        readonly=True,
    )

    sid_unit_weight_po_line = fields.Float(
        string="Peso Unitario (po)",
        related="sid_unit_weight_product",
        store=True,
        readonly=False,
    )

    sid_weight_subtotal = fields.Float(
        string="Peso Total",
        compute="_compute_sid_weight_subtotal",
        store=True,
        readonly=True,
    )

    @api.depends("qty_to_invoice", "qty_received", "product_qty", "qty_invoiced")
    def _compute_sid_invoice(self):
        for line in self:
            qty_to_invoice = round(line.qty_to_invoice or 0.0, 2)
            qty_invoiced = round(line.qty_invoiced or 0.0, 2)
            qty_received = round(line.qty_received or 0.0, 2)
            product_qty = round(line.product_qty or 0.0, 2)

            if qty_to_invoice > 0:
                line.sid_invoice = "facturar"
            elif qty_to_invoice < 0:
                line.sid_invoice = "abono"
            elif qty_invoiced == qty_received and qty_invoiced >= product_qty:
                line.sid_invoice = "facturado"
            else:
                line.sid_invoice = "pendiente"

    @api.depends("product_qty", "qty_received")
    def _compute_pending_line(self):
        for line in self:
            product_qty = round(line.product_qty or 0.0, 2)
            qty_received = round(line.qty_received or 0.0, 2)
            line.pending_line = "true" if product_qty > qty_received else "false"

    @api.depends("qty_received", "product_qty", "sid_unit_weight_po_line")
    def _compute_sid_weight_subtotal(self):
        for line in self:
            qty_received = line.qty_received or 0.0
            product_qty = line.product_qty or 0.0
            unit_w = line.sid_unit_weight_po_line or 0.0
            qty = qty_received if qty_received > product_qty else product_qty
            line.sid_weight_subtotal = unit_w * qty
