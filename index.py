# main.py
productos = []

def menu():
    print("\n=====Sistema de Gestión de Compras =====")
    print("1. Agregar producto")
    print("2. Ver todos los productos")
    print("3. Calcular total de la compra")
    print("4. Filtrar productos por precio")
    print("5. Salir")
    return input("Selecciona una opción: ")

def agregar_producto():
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto: $"))
    productos.append({"nombre": nombre, "precio": precio})
    print(f"Producto '{nombre}' agregado con precio ${precio:.2f}.")

def ver_productos():
    if len(productos) == 0:
        print(" No hay productos en la lista.")
    else:
        print("\n Lista de productos:")
        for p in productos:
            print(f"  - {p['nombre']}: ${p['precio']:.2f}")

def calcular_total():
    if len(productos) == 0:
        print(" No hay productos en la lista.")
    else:
        total = 0
        for p in productos:
            total += p["precio"]
        print(f"\n Total de la compra: ${total:.2f}")

def filtrar_por_precio():
    limite = float(input("Mostrar productos mayores a: $"))
    encontrados = []
    for p in productos:
        if p["precio"] > limite:
            encontrados.append(p)
    if len(encontrados) == 0:
        print(" Ningún producto supera ese precio.")
    else:
        print(f"\n Productos mayores a ${limite:.2f}:")
        for p in encontrados:
            print(f"  - {p['nombre']}: ${p['precio']:.2f}")

while True:
    opcion = menu()
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        ver_productos()
    elif opcion == "3":
        calcular_total()
    elif opcion == "4":
        filtrar_por_precio()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print(" Opción no válida, intenta de nuevo.")