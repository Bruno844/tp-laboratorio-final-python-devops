import pytest
from modelos.biblioteca import Biblioteca
from modelos.material import Libro
from modelos.usuario import Usuario
from utils.excepciones import EntidadNoEncontradaError, ValorInvalidoError

def test_flujo_completo_biblioteca():
    b = Biblioteca("Biblioteca Test")
    l = Libro("L01", "1984", "George Orwell", 328, "Distopía")
    u = Usuario("U01", "Pedro", "pedro@mail.com")
    
    b.agregar_material(l)
    b.agregar_usuario(u)
    
    dias = b.registrar_prestamo("U01", "L01")
    assert dias == 14
    assert l.disponible is False
    
    b.registrar_devolucion("U01", "L01")
    assert l.disponible is True

def test_busqueda_entidad_inexistente():
    b = Biblioteca("Biblioteca Test")
    with pytest.raises(EntidadNoEncontradaError):
        b.buscar_material("NO_EXISTE")
    with pytest.raises(EntidadNoEncontradaError):
        b.buscar_usuario("NO_EXISTE")
