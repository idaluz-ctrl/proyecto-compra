# main.py
productos = []

def menu():
    print("\n===== 🛒 Sistema de Gestión de Compras =====")
    print("1. Agregar producto")
    print("2. Ver todos los productos")
    print("3. Calcular total de la compra")
    print("4. Filtrar productos por precio")
    print("5. Salir")
    return input("Selecciona una opción: ")

while True:
    opcion = menu()
    if opcion == "5":
        print("¡Hasta luego!")
        break