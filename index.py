
productos = []

def agregar_producto():
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: $"))
    productos.append({"nombre": nombre, "precio": precio})
    print(f"'{nombre}' agregado correctamente.")

def ver_productos():
    if len(productos) == 0:
        print("No hay productos registrados.")
    else:
        print("\n Lista de productos:")
        for i, p in enumerate(productos, 1):
            print(f"{i}. {p['nombre']} - ${p['precio']:.2f}")

def menu():
    print("\n===== Sistema de Gestión de Compras =====")
    print("1. Agregar producto")
    print("2. Ver todos los productos")
    print("3. Calcular total de la compra")
    print("4. Filtrar productos por precio")
    print("5. Salir")
    return input("Selecciona una opción: ")