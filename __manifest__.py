# -*- coding: utf-8 -*-
{
    "name": "sid_purchase_core",
    "version": "15.0.1.0.0",
    "category": "Purchases",
    "summary": "Campos core en pedidos de compra y líneas (HS, pendientes, pesos, bases, etc.).",
    "author": "oscarsidsa81",
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
    ],
    "installable": True,
    "application": False,
}
