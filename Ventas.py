# 1. Carga de Datos
ventas = [
    {"fecha": "2024-01-01", "producto": "Notebook", "cantidad": 2, "precio": 1200.00},
    {"fecha": "2024-01-01", "producto": "Mouse", "cantidad": 5, "precio": 25.00},
    {"fecha": "2024-01-02", "producto": "Teclado", "cantidad": 3, "precio": 45.00},
    {"fecha": "2024-01-02", "producto": "Laptop", "cantidad": 1, "precio": 1200.00},
    {"fecha": "2024-01-03", "producto": "Mouse", "cantidad": 10, "precio": 20.00},
    {"fecha": "2024-01-03", "producto": "Teclado", "cantidad": 2, "precio": 50.00},
    {"fecha": "2024-01-04", "producto": "Lampara", "cantidad": 3, "precio": 1100.00},
]

# 2. Cálculo de Ingresos Totales
ingresos_totales = 0
for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]

# 3. Análisis del Producto Más Vendido
ventas_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    if producto in ventas_por_producto:
        ventas_por_producto[producto] += venta["cantidad"]
    else:
        ventas_por_producto[producto] = venta["cantidad"]

producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
cantidad_mas_vendida = ventas_por_producto[producto_mas_vendido]

# 4. Promedio de Precio por Producto
precios_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    ingreso_venta = venta["cantidad"] * venta["precio"]
    cantidad = venta["cantidad"]
    
    if producto in precios_por_producto:
        suma_ingresos, suma_cantidades = precios_por_producto[producto]
        precios_por_producto[producto] = (suma_ingresos + ingreso_venta, suma_cantidades + cantidad)
    else:
        precios_por_producto[producto] = (ingreso_venta, cantidad)

# 5. Ventas por Día
ingresos_por_dia = {}
for venta in ventas:
    fecha = venta["fecha"]
    ingreso_venta = venta["cantidad"] * venta["precio"]
    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += ingreso_venta
    else:
        ingresos_por_dia[fecha] = ingreso_venta

# 6. Representación de Datos
resumen_ventas = {}
for producto in ventas_por_producto:
    suma_ingresos, suma_cantidades = precios_por_producto[producto]
    precio_prom = suma_ingresos / suma_cantidades
    
    resumen_ventas[producto] = {
        "cantidad_total": suma_cantidades,
        "ingresos_totales": suma_ingresos,
        "precio_promedio": round(precio_prom, 2)
    }