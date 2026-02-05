# sid_purchase_core

## PropÃ³sito
MÃ³dulo funcional que agrupa los **campos core** y cÃ³mputos bÃ¡sicos de compras en:
- `purchase.order`
- `purchase.order.line`

Incluye (entre otros):
- HS code (`sid_hs_code`, `sid_hs_code_po_line`)
- estados y cÃ³mputos de facturaciÃ³n (`sid_invoice`)
- lÃ­nea pendiente (`pending_line`)
- pesos (`sid_unit_weight_po_line`, `sid_weight_subtotal`)
- bases (`amount_untaxed_pending`, `amount_untaxed_total`) y fecha de recepciÃ³n texto (`sid_date_planned`)

## Vistas
Incluye vistas bÃ¡sicas no-OV:
- `views/purchase_order_basic.xml`
- `views/purchase_order_line_basic.xml`

## Dependencias
- `purchase`, `sale_management`, `delivery`
- `oct_fecha_contrato_compras`, `oct_fecha_contrato_ventas`
- `sid_sale_line_custom_fields` (para el related con venta)

## RelaciÃ³n con otros mÃ³dulos
- `sid_purchase_delay_sync`: cÃ¡lculo de retraso por lÃ­nea y sincronizaciÃ³n del flag en venta.
- `sid_purchase_extra_fields`: mÃ³dulo paraguas/meta para compatibilidad de dependencias.
