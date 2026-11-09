import pytest
from modelos.usuario import Usuario, UsuarioVIP
from modelos.material import Libro
from utils.excepciones import ValorInvalidoError, LimitePrestamosExcedidoError, MaterialNoDisponibleError

def test_usuario_limite_y_prestamo():
    u = Usuario("U01", "Juan", "juan@mail.com")
    assert u.limite_prestamos() == 3
    
    l1 = Libro("L01", "L1", "A1", 100, "G")
    l2 = Libro("L02", "L2", "A2", 100, "G")
    l3 = Libro("L03", "L3", "A3", 100, "G")
    l4 = Libro("L04", "L4", "A4", 100, "G")
    
    u.prestar_material(l1)
    u.prestar_material(l2)
    u.prestar_material(l3)
    
    assert len(u.materiales_prestados) == 3
    assert l1.disponible is False
    
    with pytest.raises(LimitePrestamosExcedidoError):
        u.prestar_material(l4)

def test_usuario_vip_limite():
    u_vip = UsuarioVIP("U02", "Maria VIP", "maria@mail.com", "VIP-123")
    assert u_vip.limite_prestamos() == 7

def test_devolucion_material():
    u = Usuario("U01", "Juan", "juan@mail.com")
    l = Libro("L01", "Libro Test", "Autor", 150, "Drama")
    u.prestar_material(l)
    assert l.disponible is False
    
    u.devolver_material("L01")
    assert l.disponible is True
    assert len(u.materiales_prestados) == 0
