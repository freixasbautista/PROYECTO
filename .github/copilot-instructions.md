
# Instrucciones de Copilot Agent para StockFlow Backend

## 1. Alcance y Contexto del Proyecto
Este repositorio (`stockflow_backend`) contiene el backend y la API REST para el sistema de gestión de inventarios **StockFlow** [7].
- **Idioma obligatorio**: Toda la documentación, comentarios de código y respuestas deben estar en español [9].
- **Límite de exploración**: Todo el análisis y la generación de código deben limitarse estrictamente a esta carpeta y sus subdirectorios [6].

## 2. Arquitectura de Software (Clean Architecture en 4 Capas)
Debes respetar rigurosamente la separación de responsabilidades entre capas [3]:

1. `models/` (Capa de Dominio / Modelo):
   - Contiene las entidades puras de negocio (`producto.py`, `stock.py`, `movimiento_stock.py`).
   - **POO Defensiva y Consistencia**: Validar parámetros en el constructor (`__init__`) y lanzar excepciones explícitas (`ValueError`, `TypeError`) ante datos inválidos o vacíos [4].
   - **Encapsulamiento**: Proteger atributos internos (`_atributo`) y controlar la modificación mediante `@property` y `@setter`.
   - **REGLA ESTRICTA**: No importar repositorios, servicios ni librerías web (Flask) dentro de los modelos.

2. `services/` (Capa de Aplicación / Servicios):
   - Contiene la lógica de casos de uso (`inventario_service.py`, `movimiento_service.py`).
   - Orquesta la interacción entre modelos y repositorios.
   - Aplica reglas globales de negocio:
     * Verificar que el producto esté **activo** antes de procesar movimientos.
     * Verificar **stock suficiente** para salidas.
     * Ejecutar transacciones con control de reversión (*rollback*) ante errores.
     * Emitir alertas automáticas cuando el saldo caiga por debajo del stock mínimo.

3. `repositories/` (Capa de Persistencia):
   - Operaciones CRUD (`producto_repository.py`, `movimiento_repository.py`).
   - **Seguridad**: Uso obligatorio de consultas SQL parametrizadas para evitar inyecciones SQL.

4. `app.py` (Capa de Presentación / API REST):
   - Controladores HTTP en Flask (`GET`, `POST`, `PUT`, `DELETE`) en formato JSON.
   - Manejo de códigos de estado HTTP estandarizados (`200 OK`, `201 Created`, `400 Bad Request`, `409 Conflict`, `500 Internal Server Error`).

5. `tests/` (Pruebas Automatizadas):
   - Suites de pruebas con Pytest (`test_models.py`, `test_services.py`) [2, 10].

## 3. Metodología de Desarrollo y Validación
- **TDD (Test-Driven Development)**: Al crear o modificar funcionalidades, escribir o actualizar primero las pruebas unitarias en `tests/` y validar su ejecución mediante `pytest` [2, 11].
- **Type Hints &amp; Docstrings**: Todo el código generado debe llevar anotaciones de tipos explícitas y documentación breve de funciones [4, 5].
- **Sin variables globales**: Mantener el código desacoplado y libre de efectos secundarios impuros [5, 12].

---

### 2\. Código para `.github/skills/python-dev/SKILL.md` (o