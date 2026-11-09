# 📚 Sistema de Gestión de Biblioteca (POO Python)

> Mini sistema interactivo de gestión de biblioteca desarrollado en Python aplicando principios avanzados de **Programación Orientada a Objetos (POO)**, manejo de excepciones, persistencia en memoria, generación de reportes en PDF y pruebas unitarias con `pytest`.

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)

---

## 📋 Tablas de Contenidos
- [Características Principales](#-características-principales)
- [Principios de POO Aplicados](#-principios-de-poo-aplicados)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación y Configuración](#-instalación-y-configuración)
- [Uso e Interfaz de Usuario](#-uso-e-interfaz-de-usuario)
- [Ejecución de Pruebas Unitarias](#-ejecución-de-pruebas-unitarias)

---

## ✨ Características Principales
- 📖 **Gestión de Materiales**: Registro, consulta y préstamo de libros y revistas.
- 👥 **Gestión de Usuarios**: Registro de usuarios estándar y usuarios VIP (con límites ampliados).
- 🔄 **Polimorfismo en Préstamos**: Cálculo dinámico de períodos de préstamo y penalizaciones por mora según la entidad.
- 📄 **Reportes PDF**: Exportación automática de resúmenes del sistema a formato PDF (`reporte_biblioteca.pdf`).
- 🛡️ **Manejo Robusto de Errores**: Captura de excepciones personalizadas y validación estricta con bloques `try-except`.
- 🧪 **Suite de Pruebas**: Cobertura completa de la lógica de negocio con `pytest`.

---

## 🏛️ Principios de POO Aplicados

1. **Abstracción**:
   - Clase base abstracta `Material` que encapsula campos esenciales (`id_material`, `titulo`, `autor`, `disponible`).
   - Clase base abstracta `Usuario` con comportamiento encapsulado para la gestión de ítems prestados.
2. **Encapsulamiento**:
   - Todos los atributos son privados (`__atributo`).
   - Acceso y modificación segura a través de decoradores `@property` (getters) y `@atributo.setter` (setters) con validaciones.
3. **Herencia**:
   - `Libro` y `Revista` heredan de `Material`.
   - `UsuarioVIP` hereda de `Usuario`.
4. **Polimorfismo**:
   - Redefinición del método `calcular_dias_prestamo()` y `obtener_detalle()` en `Libro` y `Revista`.
   - Redefinición de `limite_prestamos()` en `Usuario` y `UsuarioVIP`.

---

## 📁 Estructura del Proyecto

```text
sistema_biblioteca/
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
├── modelos/
│   ├── __init__.py
│   ├── material.py
│   ├── usuario.py
│   └── biblioteca.py
├── utils/
│   ├── __init__.py
│   ├── excepciones.py
│   └── pdf_generator.py
└── tests/
    ├── __init__.py
    ├── test_material.py
    ├── test_usuario.py
    └── test_biblioteca.py
```

---

## 🚀 Requisitos Previos

- Python 3.10 o superior.
- Administrador de paquetes `pip`.

---

## ⚙️ Instalación y Configuración

1. **Clonar o descargar el repositorio**:
   ```bash
   git clone https://github.com/usuario/sistema-biblioteca.git
   cd sistema-biblioteca
   ```

2. **Crear y activar el entorno virtual (`venv`)**:
   - **Linux / macOS**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - **Windows (PowerShell)**:
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Uso e Interfaz de Usuario

Para ejecutar la aplicación interactiva:

```bash
python main.py
```

### Menú Interactivo:
```text
==================================================
      📚 SISTEMA DE GESTIÓN DE BIBLIOTECA 📚
==================================================
1. Registrar Material (Libro / Revista)
2. Registrar Usuario (Estándar / VIP)
3. Prestar Material
4. Devolver Material
5. Visualizar Estado de la Biblioteca
6. Exportar Informe a PDF
7. Salir
==================================================
```

---

## 🧪 Ejecución de Pruebas Unitarias

Para ejecutar todas las pruebas y verificar el correcto funcionamiento del sistema:

```bash
pytest -v
```

Para generar un informe de cobertura (opcional):
```bash
pytest --cov=modelos --cov=utils
```


## 👤 Autor

Proyecto académico de Programación Orientada a Objetos.

**Bruno Ruiz** - Técnico Superior en DevOps, ITS Cipolletti

GitHub: [@Bruno844](https://github.com/Bruno844)
