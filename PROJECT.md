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

# 2. Alcance del Proyecto

Este apartado define los límites de la primera versión (**MVP**) para evitar el *scope creep* y mantener el foco en el núcleo operativo del inventario.

# 2. Alcance — qué incluye y qué NO incluye

Esto es lo que evita que el proyecto se convierta en algo interminable.

### Incluido en el proyecto
- Gestión de productos y categorías.
- Control de existencias.
- Registro de entradas, salidas y ajustes.
- Historial de movimientos.
- Alertas de reposición.
- Estadísticas básicas de inventario.
- Backend, base de datos, API y frontend.
- Testing automatizado.

### Fuera del alcance inicial
- Facturación electrónica.
- Integración con AFIP/ARCA.
- Gestión de empleados.
- Contabilidad.
- Integración con proveedores externos.
- E-commerce.
- Múltiples sucursales.
- Sistema de pagos.
- Aplicación móvil nativa.

> Esto no significa que nunca lo vas a hacer. Significa que no forma parte de la primera versión, evitando expandir el proyecto constantemente.

---

# 3. Requisitos funcionales — qué tiene que poder hacer

Acá describís las capacidades del sistema desde el punto de vista del usuario, sin explicar todavía cómo las vas a programar.

| Módulo | Requisitos |
| :--- | :--- |
| **RF-01 — Gestión de productos** | • Crear productos.<br>• Consultar listado y detalles.<br>• Editar información.<br>• Buscar por nombre o SKU.<br>• Filtrar por categoría o estado.<br>• Desactivar productos. |
| **RF-02 — Gestión de categorías** | • Crear categorías.<br>• Editar categorías.<br>• Consultar categorías.<br>• Asociar productos a categorías. |
| **RF-03 — Gestión de movimientos** | • Registrar entradas.<br>• Registrar salidas.<br>• Registrar ajustes.<br>• Consultar historial.<br>• Filtrar movimientos por producto, tipo o período. |
| **RF-04 — Control de stock** | • Consultar stock actual por producto.<br>• Consultar stock total.<br>• Identificar productos con stock bajo.<br>• Detectar productos sin stock. |
| **RF-05 — Dashboard** | • Visualizar métricas principales.<br>• Consultar movimientos recientes.<br>• Ver productos que requieren reposición.<br>• Consultar productos con mayor movimiento. |
| **RF-06 — Reportes** | • Consultar entradas y salidas por período.<br>• Obtener resumen de movimientos.<br>• Consultar productos según su nivel de stock.<br>• Visualizar estadísticas básicas. |

### Detalle por módulo

#### RF-01 — Gestión de productos
- Crear productos.
- Consultar listado y detalles.
- Editar información.
- Buscar por nombre o SKU.
- Filtrar por categoría o estado.
- Desactivar productos.

#### RF-02 — Gestión de categorías
- Crear categorías.
- Editar categorías.
- Consultar categorías.
- Asociar productos a categorías.

#### RF-03 — Gestión de movimientos
- Registrar entradas.
- Registrar salidas.
- Registrar ajustes.
- Consultar historial.
- Filtrar movimientos por producto, tipo o período.

#### RF-04 — Control de stock
- Consultar stock actual por producto.
- Consultar stock total.
- Identificar productos con stock bajo.
- Detectar productos sin stock.

#### RF-05 — Dashboard
- Visualizar métricas principales.
- Consultar movimientos recientes.
- Ver productos que requieren reposición.
- Consultar productos con mayor movimiento.

#### RF-06 — Reportes
- Consultar entradas y salidas por período.
- Obtener resumen de movimientos.
- Consultar productos según su nivel de stock.
- Visualizar estadísticas básicas.

# 4. Requisitos No Funcionales (RNF)

Definen los atributos de calidad, restricciones y comportamiento operativo del sistema más allá de las funcionalidades específicas.

| ID | Requisito | Descripción |
| :--- | :--- | :--- |
| **RNF-01** | **Integridad** | Los datos del stock y sus movimientos deben permanecer consistentes. |
| **RNF-02** | **Usabilidad** | La interfaz debe ser clara y permitir realizar las operaciones habituales sin confusión. |
| **RNF-03** | **Rendimiento** | Las consultas habituales de productos y movimientos deben responder sin demoras innecesarias. |
| **RNF-04** | **Mantenibilidad** | El código debe estar organizado en módulos y responsabilidades separadas. |
| **RNF-05** | **Confiabilidad** | Los errores deben gestionarse sin dejar operaciones incompletas o datos inconsistentes. |
| **RNF-06** | **Compatibilidad** | La aplicación web debe poder utilizarse desde navegadores de escritorio modernos. |
| **RNF-07** | **Seguridad** | Las entradas del usuario deben validarse y las operaciones no autorizadas deben impedirse. |

---

### Detalle por requisito no funcional

- **RNF-01 — Integridad:** Los datos del stock y sus movimientos deben permanecer consistentes.
- **RNF-02 — Usabilidad:** La interfaz debe ser clara y permitir realizar las operaciones habituales sin confusión.
- **RNF-03 — Rendimiento:** Las consultas habituales de productos y movimientos deben responder sin demoras innecesarias.
- **RNF-04 — Mantenibilidad:** El código debe estar organizado en módulos y responsabilidades separadas.
- **RNF-05 — Confiabilidad:** Los errores deben gestionarse sin dejar operaciones incompletas o datos inconsistentes.
- **RNF-06 — Compatibilidad:** La aplicación web debe poder utilizarse desde navegadores de escritorio modernos.
- **RNF-07 — Seguridad:** Las entradas del usuario deben validarse y las operaciones no autorizadas deben impedirse.
