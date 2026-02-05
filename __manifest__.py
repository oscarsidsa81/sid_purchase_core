# -*- coding: utf-8 -*-
{
    "name": "SIDSA - Purchase Core Fields",
    "version": "15.0.1.0.0",
    "category": "Purchases",
    "summary": "Campos core en pedidos de compra y lÃ­neas (HS, pendientes, pesos, bases, etc.).",
    "author": "SIDSA / Custom",
    "license": "LGPL-3",
    "depends": [
        "purchase",
        "sale_management",
        "delivery",
        "oct_fecha_contrato_compras",
        "oct_fecha_contrato_ventas",
        "sid_sale_line_custom_fields"
    ],
    "data": [
        "views/purchase_order_basic.xml",
        "views/purchase_order_line_basic.xml"
    ],
    "installable": True,
    "application": False,
}
