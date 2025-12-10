import sqlite3

#instanciamos un nombre para la base de datos
DB_NAME = 'inventario.db'

#armamos la conexión directa con sql a partir del nombre dado
def conectar():
    return sqlite3.connect(DB_NAME)

#creamos una tabla con los debidos valores de cada producto
def inicializar_db():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL,
                categoria TEXT
            )
        ''')
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error CRÍTICO en DB: {e}")

# --- FUNCIONES ---

#agrega un nuevo producto al inventario
def insertar(nombre, descripcion, cantidad, precio, categoria):
    try:
        conn = conectar()
        cursor = conn.cursor()
        query = '''INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) 
                   VALUES (?, ?, ?, ?, ?)'''
        cursor.execute(query, (nombre, descripcion, cantidad, precio, categoria))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error DB: {e}")
        return False

#funcion que permite mostrar todos los productos del inventario
def obtener_todos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    datos = cursor.fetchall()
    conn.close()
    return datos

#busca a un producto por su id asignada
def buscar_por_id(id_prod):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id_prod,))
    dato = cursor.fetchone()
    conn.close()
    return dato

#modifica un atributo de un producto
def actualizar(id_prod, nombre, desc, cant, precio, cat):
    try:
        conn = conectar()
        cursor = conn.cursor()
        query = '''UPDATE productos SET 
                   nombre=?, descripcion=?, cantidad=?, precio=?, categoria=?
                   WHERE id=?'''
        cursor.execute(query, (nombre, desc, cant, precio, cat, id_prod))
        conn.commit()
        conn.close()
        return True
    except Exception:
        return False

#permite la eliminacion de un producto
def eliminar(id_prod):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (id_prod,))
        conn.commit()
        conn.close()
        return True
    except Exception:
        return False

#muestra los productos que tienen un stock menor al indicado por el usuario.
def filtrar_por_stock(limite):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
    datos = cursor.fetchall()
    conn.close()
    return datos