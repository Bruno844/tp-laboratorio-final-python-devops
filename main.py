import os
from modelos.biblioteca import Biblioteca
from modelos.material import Libro, Revista
from modelos.usuario import Usuario, UsuarioVIP
from utils.excepciones import BibliotecaError
from utils.pdf_generator import generar_pdf_informe

def precargar_datos(biblio: Biblioteca):
    """Inicializa la biblioteca con algunos datos de muestra."""
    try:
        biblio.agregar_material(Libro("L001", "Cien Años de Soledad", "Gabriel García Márquez", 471, "Novela"))
        biblio.agregar_material(Libro("L002", "Don Quijote de la Mancha", "Miguel de Cervantes", 863, "Clásico"))
        biblio.agregar_material(Revista("R001", "National Geographic", "Editorial NatGeo", 205, "Mensual"))
        
        biblio.agregar_usuario(Usuario("U001", "Carlos Gómez", "carlos@example.com"))
        biblio.agregar_usuario(UsuarioVIP("U002", "Ana Martínez", "ana.vip@example.com", "VIP-9988"))
    except Exception as e:
        print(f"Error cargando datos iniciales: {e}")

def mostrar_menu():
    print("\n" + "="*50)
    print("      📚 SISTEMA DE GESTIÓN DE BIBLIOTECA 📚")
    print("="*50)
    print("1. Registrar Material (Libro / Revista)")
    print("2. Registrar Usuario (Estándar / VIP)")
    print("3. Prestar Material")
    print("4. Devolver Material")
    print("5. Visualizar Estado de la Biblioteca")
    print("6. Exportar Informe a PDF")
    print("7. Salir")
    print("="*50)
