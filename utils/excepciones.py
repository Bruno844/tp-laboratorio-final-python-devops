class BibliotecaError(Exception):
    """Excepción base para errores del sistema de biblioteca."""
    pass

class MaterialNoDisponibleError(BibliotecaError):
    """Se lanza cuando un material ya está prestado."""
    pass

class LimitePrestamosExcedidoError(BibliotecaError):
    """Se lanza cuando un usuario alcanza su límite de préstamos."""
    pass

class EntidadNoEncontradaError(BibliotecaError):
    """Se lanza cuando un usuario o material no existe en los arreglos."""
    pass

class ValorInvalidoError(BibliotecaError):
    """Se lanza cuando se ingresan datos con formato o valor no permitido."""
    pass
