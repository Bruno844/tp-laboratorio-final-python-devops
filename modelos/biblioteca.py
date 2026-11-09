from utils.excepciones import EntidadNoEncontradaError, ValorInvalidoError

class Biblioteca:
    """Clase gestora que administra los arreglos en memoria de materiales y usuarios."""
    def __init__(self, nombre: str):
        if not nombre:
            raise ValorInvalidoError("El nombre de la biblioteca es requerido.")
        self.__nombre = nombre
        self.__materiales = []  # Arreglo en memoria
        self.__usuarios = []    # Arreglo en memoria

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not valor:
            raise ValorInvalidoError("El nombre no puede estar vacío.")
        self.__nombre = valor

    @property
    def materiales(self) -> list:
        return list(self.__materiales)

    @property
    def usuarios(self) -> list:
        return list(self.__usuarios)

    def agregar_material(self, material) -> None:
        if any(m.id_material == material.id_material for m in self.__materiales):
            raise ValorInvalidoError(f"Ya existe un material registrado con el ID {material.id_material}.")
        self.__materiales.append(material)

    def agregar_usuario(self, usuario) -> None:
        if any(u.id_usuario == usuario.id_usuario for u in self.__usuarios):
            raise ValorInvalidoError(f"Ya existe un usuario registrado con el ID {usuario.id_usuario}.")
        self.__usuarios.append(usuario)

    def buscar_material(self, id_material: str):
        for m in self.__materiales:
            if m.id_material == id_material:
                return m
        raise EntidadNoEncontradaError(f"No se encontró el material con ID '{id_material}'.")

    def buscar_usuario(self, id_usuario: str):
        for u in self.__usuarios:
            if u.id_usuario == id_usuario:
                return u
        raise EntidadNoEncontradaError(f"No se encontró el usuario con ID '{id_usuario}'.")

    def registrar_prestamo(self, id_usuario: str, id_material: str) -> int:
        usuario = self.buscar_usuario(id_usuario)
        material = self.buscar_material(id_material)
        
        usuario.prestar_material(material)
        return material.calcular_dias_prestamo()

    def registrar_devolucion(self, id_usuario: str, id_material: str) -> None:
        usuario = self.buscar_usuario(id_usuario)
        usuario.devolver_material(id_material)
