# Sistema de Gestión de Inventario

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey?style=for-the-badge&logo=sqlite)
![Status](https://img.shields.io/badge/Estado-Finalizado-green?style=for-the-badge)

Sistema de gestión de stock de productos desarrollado en Python. Permite administrar un inventario completo utilizando una base de datos **SQLite** para la persistencia de datos y una interfaz de consola interactiva mejorada con **Colorama**.

## Funcionalidades

El sistema cumple con un CRUD completo y reportes adicionales:

* **Registrar:** Alta de productos con validación de tipos de datos.
* **Consultar:** Visualización de tabla completa de productos.
* **Buscar:** Búsqueda específica por ID único.
* **Actualizar:** Modificación de campos (Nombre, Descripción, Precio, Stock) manteniendo valores previos si se desea.
* **Eliminar:** Baja física de productos por ID.
* **Reporte:** Filtrado de productos con bajo stock (límite definido por usuario).

## Estructura del Proyecto

El código sigue el principio de **Separación de Responsabilidades** (MVC simplificado):

* `database.py`: Manejo exclusivo de conexiones y queries SQL.
* `funciones.py`: Lógica de interfaz, validaciones y menús (UI).
* `main.py`: Punto de entrada y orquestador del ciclo de vida de la app.

## Requisitos

* Python 3.x
* Librería externa: `colorama`

## Instalación y Uso

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/Aainor/ProyectoInventario.git
    cd ProyectoInventario
    ```

2.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Ejecutar la aplicación:**
    ```bash
    python main.py
    ```
    *(La base de datos `inventario.db` se creará automáticamente en la primera ejecución).*

## Autora

* **Oriana Denisse Casas** - *Desarrollo y Documentación*

## Tutora e Instructor

* **Belén** - *Tutora en TalentoTech*
* **Nicolás Riquelme** - *Instructor en TalentoTech*
