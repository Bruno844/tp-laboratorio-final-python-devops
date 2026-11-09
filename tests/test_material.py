import pytest
from modelos.material import Libro, Revista
from utils.excepciones import ValorInvalidoError

def test_creacion_libro_valida():
    l = Libro("L01", "Rayuela", "Julio Cortázar", 600, "Novela")
    assert l.id_material == "L01"
    assert l.titulo == "Rayuela"
    assert l.calcular_dias_prestamo() == 21
    assert l.disponible is True

def test_libro_atributos_invalidos():
    with pytest.raises(ValorInvalidoError):
        Libro("", "Titulo", "Autor", 100, "Genero")
    with pytest.raises(ValorInvalidoError):
        Libro("L01", "Titulo", "Autor", -5, "Genero")

def test_revista_polimorfismo():
    r = Revista("R01", "Tech Monthly", "Editorial X", 42, "Mensual")
    assert r.calcular_dias_prestamo() == 7
    assert "[REVISTA]" in r.obtener_detalle()

def test_setters_encapsulamiento():
    l = Libro("L01", "Título Inicial", "Autor", 100, "Ficción")
    l.titulo = "Título Nuevo"
    assert l.titulo == "Título Nuevo"
    with pytest.raises(ValorInvalidoError):
        l.titulo = ""
