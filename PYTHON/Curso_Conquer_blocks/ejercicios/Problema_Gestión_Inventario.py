"""
Imagina que trabajas en una empresa de logística y tu tarea es desarrollar un
sistema de gestión de inventario. El inventario está representado como una lista
de productos ordenados por sus códigos. Cada producto se describe como un
diccionario con las claves 'codigo' y 'cantidad' .
Tu objetivo es implementar una función recursiva que realice una búsqueda
binaria en este inventario y devuelva la cantidad disponible para un producto
específico, dado su código.
"""

inventario = [
    {'codigo': 'A001', 'cantidad': 50},
    {'codigo': 'A002', 'cantidad': 30},
    {'codigo': 'A003', 'cantidad': 20},
    {'codigo': 'A004', 'cantidad': 50},
    {'codigo': 'A005', 'cantidad': 30},
    {'codigo': 'A006', 'cantidad': 20},
    {'codigo': 'A007', 'cantidad': 50},
    {'codigo': 'A008', 'cantidad': 30},
    {'codigo': 'A009', 'cantidad': 20},
    {'codigo': 'A010', 'cantidad': 50},
    {'codigo': 'A011', 'cantidad': 30},
    {'codigo': 'A012', 'cantidad': 20},
    {'codigo': 'A013', 'cantidad': 50},
    {'codigo': 'A014', 'cantidad': 30},
    {'codigo': 'A015', 'cantidad': 20},
]

def busqueda_binaria(inventario, codigo, inicio=0, fin=None):
    if fin is None:
        fin = len(inventario) - 1

    if inicio > fin:
        return None  # El código no se encuentra en el inventario

    medio = (inicio + fin) // 2
    producto = inventario[medio]

    if producto['codigo'] == codigo:
        return producto
    elif producto['codigo'] < codigo:
        return busqueda_binaria(inventario, codigo, medio + 1, fin)
    else:
        return busqueda_binaria(inventario, codigo, inicio, medio - 1)


codigo_a_buscar = input("ingrese un codigo de busqueda\nEJEMPLO 'A002'")
resultado = busqueda_binaria(inventario, codigo_a_buscar)

if resultado:
    print(f"Producto encontrado: {resultado}")
else:
    print("Producto no encontrado")

