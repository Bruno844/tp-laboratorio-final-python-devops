from abc import ABC, abstractmethod
from utils.excepciones import ValorInvalidoError

class Material(ABC):
    """Clase base abstracta que representa un material bibliográfico."""
    def __init__(self, id_material: str, titulo: str, autor: str):
        if not id_material or not isinstance(id_material, str):
            raise ValorInvalidoError("El ID del material debe ser una cadena no vacía.")
        if not titulo or not isinstance(titulo, str):
            raise ValorInvalidoError("El título debe ser una cadena no vacía.")
        if not autor or not isinstance(autor, str):
            raise ValorInvalidoError("El autor debe ser una cadena no vacía.")
            
        self.__id_material = id_material
        self.__titulo = titulo
        self.__autor = autor
        self.__disponible = True

    @property
    def id_material(self) -> str:
        return self.__id_material

    @id_material.setter
    def id_material(self, valor: str):
        if not valor or not isinstance(valor, str):
            raise ValorInvalidoError("El ID debe ser un texto válido.")
        self.__id_material = valor

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, valor: str):
        if not valor or not isinstance(valor, str):
            raise ValorInvalidoError("El título debe ser un texto válido.")
        self.__titulo = valor

    @property
    def autor(self) -> str:
        return self.__autor

    @autor.setter
    def autor(self, valor: str):
        if not valor or not isinstance(valor, str):
            raise ValorInvalidoError("El autor debe ser un texto válido.")
        self.__autor = valor

    @property
    def disponible(self) -> bool:
        return self.__disponible

    @disponible.setter
    def disponible(self, valor: bool):
        if not isinstance(valor, bool):
            raise ValorInvalidoError("El estado disponible debe ser un valor booleano.")
        self.__disponible = valor

    @abstractmethod
    def calcular_dias_prestamo(self) -> int:
        pass

    @abstractmethod
    def obtener_detalle(self) -> str:
        pass


class Libro(Material):
    """Clase derivada que representa un Libro."""
    def __init__(self, id_material: str, titulo: str, autor: str, num_paginas: int, genero: str):
        super().__init__(id_material, titulo, autor)
        if not isinstance(num_paginas, int) or num_paginas <= 0:
            raise ValorInvalidoError("El número de páginas debe ser un entero positivo.")
        if not genero or not isinstance(genero, str):
            raise ValorInvalidoError("El género debe ser una cadena no vacía.")
            
        self.__num_paginas = num_paginas
        self.__genero = genero

    @property
    def num_paginas(self) -> int:
        return self.__num_paginas

    @num_paginas.setter
    def num_paginas(self, valor: int):
        if not isinstance(valor, int) or valor <= 0:
            raise ValorInvalidoError("El número de páginas debe ser un entero positivo.")
        self.__num_paginas = valor

    @property
    def genero(self) -> str:
        return self.__genero

    @genero.setter
    def genero(self, valor: str):
        if not valor or not isinstance(valor, str):
            raise ValorInvalidoError("El género debe ser un texto válido.")
        self.__genero = valor

    def calcular_dias_prestamo(self) -> int:
        # Libros extensos (> 500 pags) reciben más días
        return 21 if self.__num_paginas > 500 else 14

    def obtener_detalle(self) -> str:
        estado = "Disponible" if self.disponible else "Prestado"
        return f"[LIBRO] ID: {self.id_material} | Título: {self.titulo} | Autor: {self.autor} | Págs: {self.num_paginas} | Género: {self.genero} | Estado: {estado}"


class Revista(Material):
    """Clase derivada que representa una Revista."""
    def __init__(self, id_material: str, titulo: str, autor: str, numero_edicion: int, periodicidad: str):
        super().__init__(id_material, titulo, autor)
        if not isinstance(numero_edicion, int) or numero_edicion <= 0:
            raise ValorInvalidoError("El número de edición debe ser un entero positivo.")
        if not periodicidad or not isinstance(periodicidad, str):
            raise ValorInvalidoError("La periodicidad debe ser una cadena no vacía.")
            
        self.__numero_edicion = numero_edicion
        self.__periodicidad = periodicidad

    @property
    def numero_edicion(self) -> int:
        return self.__numero_edicion

    @numero_edicion.setter
    def numero_edicion(self, valor: int):
        if not isinstance(valor, int) or valor <= 0:
            raise ValorInvalidoError("El número de edición debe ser positivo.")
        self.__numero_edicion = valor

    @property
    def periodicidad(self) -> str:
        return self.__periodicidad

    @periodicidad.setter
    def periodicidad(self, valor: str):
        if not valor or not isinstance(valor, str):
            raise ValorInvalidoError("La periodicidad debe ser un texto válido.")
        self.__periodicidad = valor

    def calcular_dias_prestamo(self) -> int:
        return 7  # Las revistas tienen préstamo más corto

    def obtener_detalle(self) -> str:
        estado = "Disponible" if self.disponible else "Prestado"
        return f"[REVISTA] ID: {self.id_material} | Título: {self.titulo} | Edición N°: {self.numero_edicion} | Frecuencia: {self.periodicidad} | Estado: {estado}"
