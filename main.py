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



def main():
    biblio = Biblioteca("Biblioteca Central POO")
    precargar_datos(biblio)
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-7): ").strip()
        
        try:
            if opcion == "1":
                tipo = input("Tipo de material (1: Libro, 2: Revista): ").strip()
                id_m = input("ID Único: ").strip()
                titulo = input("Título: ").strip()
                autor = input("Autor / Editorial: ").strip()
                
                if tipo == "1":
                    num_p = int(input("Número de páginas: "))
                    genero = input("Género literario: ").strip()
                    libro = Libro(id_m, titulo, autor, num_p, genero)
                    biblio.agregar_material(libro)
                    print(f"✅ Libro '{titulo}' registrado exitosamente.")
                elif tipo == "2":
                    edicion = int(input("Número de edición: "))
                    period = input("Periodicidad (Mensual, Semanal, etc.): ").strip()
                    revista = Revista(id_m, titulo, autor, edicion, period)
                    biblio.agregar_material(revista)
                    print(f"✅ Revista '{titulo}' registrada exitosamente.")
                else:
                    print("⚠️ Opción de tipo de material inválida.")

            elif opcion == "2":
                tipo_u = input("Tipo de usuario (1: Estándar, 2: VIP): ").strip()
                id_u = input("ID Único de usuario: ").strip()
                nombre = input("Nombre completo: ").strip()
                email = input("Correo electrónico: ").strip()
                
                if tipo_u == "1":
                    usr = Usuario(id_u, nombre, email)
                    biblio.agregar_usuario(usr)
                    print(f"✅ Usuario estándar '{nombre}' registrado.")
                elif tipo_u == "2":
                    cod = input("Código de Membresía VIP: ").strip()
                    usr_vip = UsuarioVIP(id_u, nombre, email, cod)
                    biblio.agregar_usuario(usr_vip)
                    print(f"✅ Usuario VIP '{nombre}' registrado.")
                else:
                    print("⚠️ Opción de tipo de usuario inválida.")

            elif opcion == "3":
                id_u = input("ID de Usuario: ").strip()
                id_m = input("ID del Material a prestar: ").strip()
                dias = biblio.registrar_prestamo(id_u, id_m)
                print(f"✅ Préstamo realizado exitosamente por {dias} días.")

            elif opcion == "4":
                id_u = input("ID de Usuario: ").strip()
                id_m = input("ID del Material a devolver: ").strip()
                biblio.registrar_devolucion(id_u, id_m)
                print(f"✅ Devolución registrada correctamente.")

            elif opcion == "5":
                print("\n--- 📖 MATERIALES REGISTRADOS ---")
                for m in biblio.materiales:
                    print(m.obtener_detalle())
                    
                print("\n--- 👥 USUARIOS REGISTRADOS ---")
                for u in biblio.usuarios:
                    print(u.obtener_info())
                    if u.materiales_prestados:
                        print("   Materiales en posesión:")
                        for mat in u.materiales_prestados:
                            print(f"    - {mat.titulo} (ID: {mat.id_material})")

            elif opcion == "6":
                nombre_pdf = generar_pdf_informe(biblio)
                print(f"📄 Informe generado con éxito: '{nombre_pdf}'")

            elif opcion == "7":
                print("👋 ¡Gracias por usar el Sistema de Biblioteca!")
                break
            else:
                print("⚠️ Opción no válida. Intente nuevamente.")
                
        except ValueError:
            print("❌ Error de formato: Asegúrese de ingresar números enteros donde se requiera.")
        except BibliotecaError as e:
            print(f"❌ Error de negocio: {e}")
        except Exception as e:
            print(f"❌ Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()
