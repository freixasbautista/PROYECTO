# REGLAS DE NEGOCIO INICIALES

1. **El stock solo cambia por movimientos [MVP]**
Nadie edita el número de stock directamente. Todo cambio (compra, venta, rotura, ajuste) se registra como un movimiento con producto, cantidad, motivo y fecha.

2. **No se permite stock negativo [MVP]**
Si intentan vender 10 unidades y hay 7, el sistema rechaza la operación con un error claro.

3. Los movimientos son inmutables
Un movimiento registrado no se edita ni se borra. Si hubo un error, se corrige con un movimiento nuevo de ajuste. Así el historial siempre es confiable.

4. **Cada movimiento exige datos obligatorios [MVP]**
Producto, tipo (entrada o salida), cantidad mayor a 0, motivo y fecha. Sin eso, no se registra.

5. **Atomicidad: todo o nada [MVP]**
Guardar el movimiento y actualizar el stock ocurren en una sola transacción. Si algo falla, no se guarda ninguna de las dos cosas.

6. Productos con historial no se eliminan
Si un producto ya tuvo movimientos, solo se puede desactivar, nunca borrar.

7. Productos inactivos no operan
No se pueden registrar entradas ni salidas sobre un producto desactivado.

8. **El SKU es único [MVP]**
No pueden existir dos productos con el mismo código identificador.

9. Alerta por stock bajo
Si el stock actual es menor al stock mínimo, el producto se marca automáticamente como "requiere reposición".

10. Protección contra duplicados
Un doble clic o un reintento no debe registrar dos veces la misma operación (por ejemplo, con un identificador único por solicitud).

11. Control de concurrencia
Si dos operaciones modifican el mismo producto casi al mismo tiempo, el resultado final debe seguir siendo correcto (sin pisarse entre sí).

12. Ajuste por inventario físico

13. **[Regla 13 pendiente de redacción] [MVP]**
Si el conteo real difiere del sistema (5 en sistema, 3 reales), se registra un movimiento de ajuste de −2 con motivo "diferencia de inventario", sin editar el stock directamente.

13. Validaciones de precios y valores
Cantidades enteras positivas, precios no negativos, y stock mínimo no negativo.
