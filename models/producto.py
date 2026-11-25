"""Entidad de dominio ``Producto``.

Capa de Modelo: Python puro. No depende de persistencia ni presentación.
"""
from __future__ import annotations

import math
from typing import Optional


class Producto:
    """Producto del inventario con invariantes garantizadas en todo momento.

    Cualquier instancia que exista es válida: los mismos validadores se usan
    en ``__init__`` y en los setters, por lo que no hay forma de dejar el
    objeto en un estado inconsistente.
    """

    def __init__(
        self,
        codigo: str,
        nombre: str,
        precio: float,
        activo: bool = True,
        id: Optional[int] = None,
    ) -> None:
        # Se asigna vía las propiedades para reutilizar las validaciones.
        self.id = id
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.activo = activo

    # ------------------------------------------------------------------ id
    @property
    def id(self) -> Optional[int]:
        return self._id

    @id.setter
    def id(self, valor: Optional[int]) -> None:
        if valor is not None:
            # bool es subclase de int: se rechaza explícitamente.
            if isinstance(valor, bool) or not isinstance(valor, int):
                raise TypeError(
                    f"El id debe ser int o None, se recibió {type(valor).__name__}."
                )
            if valor <= 0:
                raise ValueError(f"El id debe ser un entero mayor que 0, se recibió {valor}.")
        self._id = valor

    # -------------------------------------------------------------- codigo
    @property
    def codigo(self) -> str:
        return self._codigo

    @codigo.setter
    def codigo(self, valor: str) -> None:
        self._codigo = self._validar_texto(valor, "codigo")

    # ------------------------------------------------------------- nombre
    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        self._nombre = self._validar_texto(valor, "nombre")

    # ------------------------------------------------------------- precio
    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float) -> None:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError(
                f"El precio debe ser un número (float), se recibió {type(valor).__name__}."
            )
        if not math.isfinite(valor):
            raise ValueError(f"El precio debe ser un número finito, se recibió {valor}.")
        if valor < 0.0:
            raise ValueError(f"El precio no puede ser negativo, se recibió {valor}.")
        self._precio = float(valor)

    # ------------------------------------------------------------- activo
    @property
    def activo(self) -> bool:
        return self._activo

    @activo.setter
    def activo(self, valor: bool) -> None:
        if not isinstance(valor, bool):
            raise TypeError(f"activo debe ser bool, se recibió {type(valor).__name__}.")
        self._activo = valor

    # ------------------------------------------------------------ métodos
    def activar(self) -> None:
        """Marca el producto como activo."""
        self._activo = True

    def desactivar(self) -> None:
        """Marca el producto como inactivo."""
        self._activo = False

    def __repr__(self) -> str:
        return (
            f"Producto(id={self._id!r}, codigo={self._codigo!r}, "
            f"nombre={self._nombre!r}, precio={self._precio!r}, activo={self._activo!r})"
        )

    # ------------------------------------------------------------ helpers
    @staticmethod
    def _validar_texto(valor: str, campo: str) -> str:
        """Valida que sea str no vacío y devuelve el valor sin espacios sobrantes."""
        if not isinstance(valor, str):
            raise TypeError(f"{campo} debe ser str, se recibió {type(valor).__name__}.")
        limpio = valor.strip()
        if not limpio:
            raise ValueError(f"{campo} no puede estar vacío ni contener solo espacios.")
        return limpio