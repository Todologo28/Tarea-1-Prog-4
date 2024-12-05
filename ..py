import sqlite3

# Crear o conectar a la base de datos SQLite
conn = sqlite3.connect('libro_recetas.db')
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS recetas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    ingredientes TEXT NOT NULL,
                    pasos TEXT NOT NULL)''')

# Función para agregar una nueva receta
def agregar_receta():
    nom = input("Nombre de la receta: ")
    ingredientes = input("Ingredientes (separados por comas): ")
    pasos = input("Pasos para la receta: ")

    # Almacenar en la base de datos
    cursor.execute("INSERT INTO recetas (nombre, ingredientes, pasos) VALUES (?, ?, ?)",
                   (nom, ingredientes, pasos))
    conn.commit()
    print("Receta agregada con éxito.")

# Función para actualizar una receta existente
def actualizar_receta():
    receta_id = input("ID de la receta a actualizar: ")
    nom = input("Nuevo nombre de la receta: ")
    ingredientes = input("Nuevos ingredientes (separados por comas): ")
    pasos = input("Nuevos pasos: ")

    # Actualizar en la base de datos
    cursor.execute("UPDATE recetas SET nombre = ?, ingredientes = ?, pasos = ? WHERE id = ?",
                   (nom, ingredientes, pasos, receta_id))
    conn.commit()
    print("Receta actualizada con éxito.")

# Función para eliminar una receta
def eliminar_receta():
    receta_id = input("ID (número al lado izquierdo de la receta) de la receta a eliminar: ")

    # Eliminar de la base de datos
    cursor.execute("DELETE FROM recetas WHERE id = ?", (receta_id,))
    conn.commit()
    print("Receta eliminada con éxito.")

# Función para ver el listado de recetas
def ver_recetas():
    # Obtener todas las recetas de la base de datos
    cursor.execute("SELECT id, nombre FROM recetas")
    recetas = cursor.fetchall()

    if recetas:
        print("Listado de recetas:")
        for receta in recetas:
            print(f"{receta[0]}: {receta[1]}")
    else:
        print("No hay recetas disponibles.")

# Función para buscar ingredientes y pasos de una receta
def buscar_receta():
    nombre = input("Nombre de la receta a buscar: ")

    # Buscar en la base de datos
    cursor.execute("SELECT ingredientes, pasos FROM recetas WHERE nombre = ?", (nombre,))
    resultado = cursor.fetchone()

    if resultado:
        print(f"Ingredientes: {resultado[0]}")
        print(f"Pasos: {resultado[1]}")
    else:
        print("Receta no encontrada.")

# Función principal que ejecuta el menú
def menu():
    while True:
        print("\n--- Libro de Recetas ---")
        print("1. Agregar nueva receta")
        print("2. Actualizar receta existente")
        print("3. Eliminar receta")
        print("4. Ver listado de recetas")
        print("5. Buscar ingredientes y pasos de receta")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            agregar_receta()
        elif opcion == '2':
            actualizar_receta()
        elif opcion == '3':
            eliminar_receta()
        elif opcion == '4':
            ver_recetas()
        elif opcion == '5':
            buscar_receta()
        elif opcion == '6':
            print("Saliendo...")
            break
        else:

            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == '__main__':
    menu()

# Cerrar la conexión a la base de datos al terminar
conn.close()
