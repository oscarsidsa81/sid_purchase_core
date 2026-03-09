# sid_purchase_core

## Propósito
Módulo funcional que agrupa los **campos core** y cómputos básicos de compras en:

- `purchase.order`
- `purchase.order.line`

Incluye (entre otros):

- HS code (`sid_hs_code`, `sid_hs_code_po_line`)
- estados y cómputos de facturación (`sid_invoice`)
- línea pendiente (`pending_line`)
- pesos (`sid_unit_weight_po_line`, `sid_weight_subtotal`)
- bases (`amount_untaxed_pending`, `amount_untaxed_total`)
- fecha de recepción en texto (`sid_date_planned`)

## Vistas
Incluye vistas básicas no-OV:

- `views/purchase_order_basic.xml`
- `views/purchase_order_line_basic.xml`

## Dependencias

- `purchase`
- `sale_management`
- `delivery`
- `oct_fecha_contrato_compras`
- `oct_fecha_contrato_ventas`
- `sid_sale_line_custom_fields` (para el related con venta)

## Relación con otros módulos

- `sid_purchase_delay_sync`: cálculo de retraso por línea y sincronización del flag en venta.
- `sid_purchase_extra_fields`: módulo paraguas/meta para compatibilidad de dependencias.