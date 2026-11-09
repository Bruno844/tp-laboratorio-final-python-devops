from utils.excepciones import ValorInvalidoError, LimitePrestamosExcedidoError, MaterialNoDisponibleError

class Usuario:
    """Clase base que representa un usuario de la biblioteca."""
    def __init__(self, id_usuario: str, nombre: str, email: str):
        if not id_usuario or not isinstance(id_usuario, str):
            raise ValorInvalidoError("El ID de usuario debe ser una cadena no vacía.")
        if not nombre or not isinstance(nombre, str):
            raise ValorInvalidoError("El nombre debe ser una cadena no vacía.")
        if not email or "@" not in email:
            raise ValorInvalidoError("El email ingresado no es válido.")
            
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__email = email
        self.__materiales_prestados = []  # Array/lista en memoria

    @property
    def id_usuario(self) -> str:
        return self.__id_usuario

    @id_usuario.setter
    def id_usuario(self, valor: str):
        if not valor or not isinstance(valor, str):
            raise ValorInvalidoError("El ID de usuario debe ser válido.")
        self.__id_usuario = valor

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not valor or not isinstance(valor, str):
            raise ValorInvalidoError("El nombre debe ser válido.")
        self.__nombre = valor

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, valor: str):
        if not valor or "@" not in valor:
            raise ValorInvalidoError("Email inválido.")
        self.__email = valor

    @property
    def materiales_prestados(self) -> list:
        return list(self.__materiales_prestados)

    def limite_prestamos(self) -> int:
        return 3

    def prestar_material(self, material) -> None:
        if len(self.__materiales_prestados) >= self.limite_prestamos():
            raise LimitePrestamosExcedidoError(f"El usuario {self.__nombre} alcanzó el límite de {self.limite_prestamos()} préstamos.")
        if not material.disponible:
            raise MaterialNoDisponibleError(f"El material '{material.titulo}' no está disponible.")
        
        material.disponible = False
        self.__materiales_prestados.append(material)

    def devolver_material(self, id_material: str) -> None:
        encontrado = None
        for mat in self.__materiales_prestados:
            if mat.id_material == id_material:
                encontrado = mat
                break
        
        if not encontrado:
            raise ValorInvalidoError(f"El usuario no tiene prestado el material con ID {id_material}.")
        
        encontrado.disponible = True
        self.__materiales_prestados.remove(encontrado)

    def obtener_info(self) -> str:
        return f"[USUARIO ESTÁNDAR] ID: {self.id_usuario} | Nombre: {self.nombre} | Email: {self.email} | Préstamos activos: {len(self.materiales_prestados)}/{self.limite_prestamos()}"


class UsuarioVIP(Usuario):
    """Usuario VIP con beneficios ampliados de préstamo."""
    def __init__(self, id_usuario: str, nombre: str, email: str, codigo_membresia: str):
        super().__init__(id_usuario, nombre, email)
        if not codigo_membresia or not isinstance(codigo_membresia, str):
            raise ValorInvalidoError("El código de membresía debe ser un texto válido.")
        self.__codigo_membresia = codigo_membresia

    @property
    def codigo_membresia(self) -> str:
        return self.__codigo_membresia

    @codigo_membresia.setter
    def codigo_membresia(self, valor: str):
        if not valor or not isinstance(valor, str):
            raise ValorInvalidoError("Código de membresía inválido.")
        self.__codigo_membresia = valor

    def limite_prestamos(self) -> int:
        return 7  # Los usuarios VIP pueden llevar más materiales

    def obtener_info(self) -> str:
        return f"[USUARIO VIP] ID: {self.id_usuario} | Nombre: {self.nombre} | Membresía: {self.codigo_membresia} | Préstamos activos: {len(self.materiales_prestados)}/{self.limite_prestamos()}"
