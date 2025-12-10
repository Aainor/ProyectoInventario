from colorama import init, Fore, Style
import database

#inicializa colorama y resetea el color automáticamente al final de cada print
init(autoreset=True)

# --- MENÚ PRINCIPAL ---
def mostrar_menu():
    print(f"\n{Fore.CYAN}{Style.BRIGHT}=== SISTEMA DE GESTIÓN DE PRODUCTOS ==={Style.RESET_ALL}")
    print(f"{Fore.YELLOW}(1).{Fore.RESET} Registrar Producto")
    print(f"{Fore.YELLOW}(2).{Fore.RESET} Mostrar Todos")
    print(f"{Fore.YELLOW}(3).{Fore.RESET} Buscar por ID")
    print(f"{Fore.YELLOW}(4).{Fore.RESET} Actualizar Producto (ID)")
    print(f"{Fore.YELLOW}(5).{Fore.RESET} Eliminar Producto (ID)")
    print(f"{Fore.YELLOW}(6).{Fore.RESET} Reporte de Bajo Stock")
    print(f"{Fore.RED}(7). Salir{Fore.RESET}")

# --- 1. REGISTRAR (Con ID automático) ---
def registrar_producto():
    print(f"\n{Fore.CYAN}--- NUEVO PRODUCTO ---")
    nombre = input("Nombre: ").strip().title()
    if not nombre: return
    
    descripcion = input("Descripción: ").strip().capitalize()
    categoria = input("Categoría: ").strip().title()

    # Validaciones siguen acá porque es responsabilidad de la UI validar input de usuario
    while True:
        try:
            precio = float(input("Precio: $"))
            if precio > 0: break
        except ValueError: pass
        print(f"{Fore.RED}⚠️ Precio inválido.")

    while True:
        try:
            cantidad = int(input("Stock inicial: "))
            if cantidad >= 0: break
        except ValueError: pass
        print(f"{Fore.RED}⚠️ Stock inválido.")

    # Llamamos a la base de datos
    if database.insertar(nombre, descripcion, cantidad, precio, categoria):
        print(f"\n{Fore.GREEN}¡Guardado con éxito!")
    else:
        print(f"\n{Fore.RED}Error al guardar en base de datos.")
    
    input(f"{Style.DIM}Enter...{Fore.RESET}")

# --- 2. MOSTRAR ---
def mostrar_productos(): 
    print(f"\n{Fore.CYAN}--- INVENTARIO ---")
    productos = database.obtener_todos() 
    
    if not productos:
        print(f"{Fore.YELLOW}⚠️ Base de datos vacía.")
    else:
        print(f"{Fore.MAGENTA}{'ID':<4} | {'NOMBRE':<20} | {'PRECIO':<10} | {'STOCK':<5} | {'CATEGORÍA'}")
        print("-" * 65)
        for p in productos:
            print(f"{p[0]:<4} | {p[1]:<20} | ${p[4]:<9.2f} | {p[3]:<5} | {p[5]}")
    
    input(f"\n{Style.DIM}Enter...{Fore.RESET}")

# --- 3. BUSCAR (Por ID) ---
def buscar_producto_id():
    print(f"\n{Fore.CYAN}--- BUSCAR POR ID ---")
    try:
        id_buscado = int(input("Ingrese ID a buscar: "))
        # next() busca el primero que coincida, si no encuentra devuelve None
        producto = database.buscar_por_id(id_buscado)

        if producto:
            print(f"\n{Fore.GREEN}✅ Encontrado:{Fore.RESET}")
            print(f"ID: {producto[0]} | Nombre: {producto[1]}")
            print(f"Descripción: {producto[2]}")
            print(f"Stock: {producto[3]} | Precio: ${producto[4]}")
        else:
            print(f"{Fore.RED}⚠️ No existe producto con ID {id_buscado}.")
    except ValueError:
        print(f"{Fore.RED}⚠️ El ID debe ser un número.")
    
    input(f"\n{Style.DIM}Enter para continuar...{Fore.RESET}")

# --- 4. ACTUALIZAR ---
def actualizar_producto():
    print(f"\n{Fore.CYAN}--- ACTUALIZAR PRODUCTO ---")
    mostrar_productos() # Muestra lista para ver qué ID elegir
    
    try:
        id_mod = int(input("\nIngrese el ID del producto a modificar: "))
        producto = database.buscar_por_id(id_mod)

        if not producto:
            print(f"{Fore.RED}⚠️ ID no encontrado.")
            return

        print(f"{Style.DIM}Deje vacío y presione Enter para mantener el valor actual.{Fore.RESET}")
        
       # Lógica de UI: Decidir qué valor queda (el nuevo o el viejo)
        nuevo_n = input(f"Nombre ({producto[1]}): ").strip().title() or producto[1]
        nuevo_d = input(f"Desc ({producto[2]}): ").strip() or producto[2]
        nuevo_c_str = input(f"Stock ({producto[3]}): ")
        nuevo_p_str = input(f"Precio ({producto[4]}): ")
        nuevo_cat = input(f"Categoría ({producto[5]}): ").strip().title() or producto[5]

        # Validar numéricos si se ingresaron
        nuevo_c = int(nuevo_c_str) if nuevo_c_str else producto[3]
        nuevo_p = float(nuevo_p_str) if nuevo_p_str else producto[4]

        if database.actualizar(id_mod, nuevo_n, nuevo_d, nuevo_c, nuevo_p, nuevo_cat):
            print(f"\n{Fore.GREEN}¡Actualizado!")
        else:
            print(f"{Fore.RED}Error al actualizar.")

    except ValueError:
        print(f"{Fore.RED}⚠️ El ID debe ser numérico.")
    
    input(f"{Style.DIM}Enter para continuar...{Fore.RESET}")

# --- 5. ELIMINAR (Por ID) ---
def eliminar_producto():
    print(f"\n{Fore.RED}--- ELIMINAR PRODUCTO ---")
    mostrar_productos()
    
    try:
        id_borrar = int(input("\nIngrese ID del producto a eliminar: "))
        # Buscamos el producto
        producto = database.buscar_por_id(id_borrar)

        if producto:
            if input(f"¿Borrar '{producto[1]}'? (s/n): ").lower() == 's':
                database.eliminar(id_borrar)
                print(f"\n{Fore.GREEN}Eliminado.")
            else:
                print(f"\n{Fore.YELLOW}Operación cancelada.")
        else:
            print(f"{Fore.RED}No se encontró ese ID.")
            
    except ValueError:
        print(f"{Fore.RED}⚠️ Error: Ingrese un número válido.")
        
    input(f"\n{Style.DIM}Enter para continuar...{Fore.RESET}")

# --- 6. REPORTE BAJO STOCK ---
def reporte_bajo_stock():
    print(f"\n{Fore.CYAN}--- REPORTE DE BAJO STOCK ---")
    try:
        limite = int(input("\nLímite de stock: "))
        lista = database.filtrar_por_stock(limite)
        
        print(f"\nProductos con stock <= {limite}:")
        print("-" * 40)
        for p in lista:
            print(f"ID: {p[0]} | {p[1]} | {Fore.RED}Stock: {p[3]}{Fore.RESET}")
    except ValueError:
        print(f"{Fore.RED}Número inválido.")
    
    input(f"{Style.DIM}Enter...{Fore.RESET}")