import pytest

from models.producto import Producto


@pytest.fixture
def producto() -> Producto:
    return Producto(codigo="SKU-001", nombre="Teclado", precio=49.99)


# ----------------------------------------------------------- caso feliz
class TestCreacion:
    def test_creacion_con_valores_por_defecto(self, producto):
        assert producto.id is None
        assert producto.codigo == "SKU-001"
        assert producto.nombre == "Teclado"
        assert producto.precio == 49.99
        assert producto.activo is True

    def test_creacion_con_todos_los_valores(self):
        p = Producto(codigo="A1", nombre="Mouse", precio=10.0, activo=False, id=7)
        assert (p.id, p.codigo, p.nombre, p.precio, p.activo) == (7, "A1", "Mouse", 10.0, False)

    def test_precio_cero_es_valido(self):
        assert Producto("A1", "Regalo", 0.0).precio == 0.0

    def test_precio_entero_se_convierte_a_float(self):
        p = Producto("A1", "Cable", 5)
        assert p.precio == 5.0 and isinstance(p.precio, float)

    def test_codigo_y_nombre_se_normalizan_sin_espacios_sobrantes(self):
        p = Producto("  SKU-9  ", "  Monitor 24  ", 100.0)
        assert p.codigo == "SKU-9"
        assert p.nombre == "Monitor 24"

    def test_repr_es_claro(self):
        p = Producto("SKU-1", "Teclado", 9.5, id=3)
        assert repr(p) == "Producto(id=3, codigo='SKU-1', nombre='Teclado', precio=9.5, activo=True)"


# ------------------------------------------------------- errores de tipo
class TestTypeError:
    @pytest.mark.parametrize("id_invalido", ["1", 1.5, True, [1]])
    def test_id_tipo_invalido(self, id_invalido):
        with pytest.raises(TypeError, match="id"):
            Producto("A1", "X", 1.0, id=id_invalido)

    @pytest.mark.parametrize("codigo", [None, 123, 1.5, ["A"]])
    def test_codigo_tipo_invalido(self, codigo):
        with pytest.raises(TypeError, match="codigo"):
            Producto(codigo, "X", 1.0)

    @pytest.mark.parametrize("nombre", [None, 123, b"x"])
    def test_nombre_tipo_invalido(self, nombre):
        with pytest.raises(TypeError, match="nombre"):
            Producto("A1", nombre, 1.0)

    @pytest.mark.parametrize("precio", ["10", None, True, [1.0]])
    def test_precio_tipo_invalido(self, precio):
        with pytest.raises(TypeError, match="precio"):
            Producto("A1", "X", precio)

    @pytest.mark.parametrize("activo", [1, 0, "True", None])
    def test_activo_tipo_invalido(self, activo):
        with pytest.raises(TypeError, match="activo"):
            Producto("A1", "X", 1.0, activo=activo)


# ------------------------------------------------------ errores de valor
class TestValueError:
    @pytest.mark.parametrize("id_invalido", [0, -1])
    def test_id_no_positivo(self, id_invalido):
        with pytest.raises(ValueError, match="id"):
            Producto("A1", "X", 1.0, id=id_invalido)

    @pytest.mark.parametrize("codigo", ["", "   ", "\t\n"])
    def test_codigo_vacio(self, codigo):
        with pytest.raises(ValueError, match="codigo"):
            Producto(codigo, "X", 1.0)

    @pytest.mark.parametrize("nombre", ["", "   "])
    def test_nombre_vacio(self, nombre):
        with pytest.raises(ValueError, match="nombre"):
            Producto("A1", nombre, 1.0)

    @pytest.mark.parametrize("precio", [-0.01, -100])
    def test_precio_negativo(self, precio):
        with pytest.raises(ValueError, match="precio"):
            Producto("A1", "X", precio)

    @pytest.mark.parametrize("precio", [float("nan"), float("inf"), float("-inf")])
    def test_precio_no_finito(self, precio):
        with pytest.raises(ValueError, match="precio"):
            Producto("A1", "X", precio)


# ---------------------------------------------------------------- setters
class TestSetters:
    def test_setters_validos(self, producto):
        producto.id = 5
        producto.codigo = " NEW "
        producto.nombre = "Otro"
        producto.precio = 0
        producto.activo = False
        assert (producto.id, producto.codigo, producto.nombre, producto.precio, producto.activo) == (
            5, "NEW", "Otro", 0.0, False,
        )

    def test_setter_id_acepta_none(self):
        p = Producto("A1", "X", 1.0, id=2)
        p.id = None
        assert p.id is None

    @pytest.mark.parametrize(
        "campo, valor, error",
        [
            ("id", 0, ValueError),
            ("id", "1", TypeError),
            ("codigo", "  ", ValueError),
            ("codigo", 5, TypeError),
            ("nombre", "", ValueError),
            ("nombre", None, TypeError),
            ("precio", -1.0, ValueError),
            ("precio", "9", TypeError),
            ("activo", "si", TypeError),
        ],
    )
    def test_setter_invalido_lanza_error(self, producto, campo, valor, error):
        with pytest.raises(error):
            setattr(producto, campo, valor)

    def test_setter_fallido_no_corrompe_el_estado(self, producto):
        with pytest.raises(ValueError):
            producto.precio = -5.0
        assert producto.precio == 49.99


# ----------------------------------------------------------- activar/desactivar
class TestEstado:
    def test_desactivar(self, producto):
        producto.desactivar()
        assert producto.activo is False

    def test_activar(self):
        p = Producto("A1", "X", 1.0, activo=False)
        p.activar()
        assert p.activo is True

    def test_son_idempotentes(self, producto):
        producto.activar()
        producto.activar()
        assert producto.activo is True
        producto.desactivar()
        producto.desactivar()
        assert producto.activo is False