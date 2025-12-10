import os
import time
from colorama import init, Fore, Style
import funciones
import database

init(autoreset=True)

def limpiar_pantalla():
    #limpia la consola, automáticamente, con un comando diferente según el sistema operativo.
    #nt = Windows New Technology
    #si el sistema operativo es windows, corre cls. sino (Linux, Mac) corre clear.
    os.system('cls' if os.name == 'nt' else 'clear')

def ejecutar_sistema():
    database.inicializar_db()
    while True:
        limpiar_pantalla()
        funciones.mostrar_menu()
        opcion = input(f"\n{Fore.GREEN}>> Seleccione una opción: {Fore.RESET}")

        if opcion == '1':
            funciones.registrar_producto()
        elif opcion == '2': 
            funciones.mostrar_productos()
        elif opcion == '3':
            funciones.buscar_producto_id() 
        elif opcion == '4':
            funciones.actualizar_producto()
        elif opcion == '5':
            funciones.eliminar_producto()
        elif opcion == '6':
            funciones.reporte_bajo_stock() 
        elif opcion == '7':
            print(f"\n{Fore.CYAN}Cerrando sistema...")
            break
        else:
            print(f"{Fore.RED} Opción inválida.")
            time.sleep(1)

if __name__ == "__main__":
    ejecutar_sistema()