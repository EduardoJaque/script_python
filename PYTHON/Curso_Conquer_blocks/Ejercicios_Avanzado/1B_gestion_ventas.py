"""Crea un programa que permita gestionar las ventas de una tienda. Utiliza una 
estructura de datos adecuada para almacenar la información de las ventas 
(por ejemplo, una lista de diccionarios). Implementa dos funciones, una para 
agregar el producto vendido con su precio y otro para mostrar las ventas de 
productos con sus respectivos precios.
 (La base de datos puede tener la forma [{“Producto”: producto1, “Precio”: 
precio1}, {“Producto”: producto2, “Precio”: precio2}…])"""
#Implementa dos funciones
lista_de_productos=[]
diccionario={}
#una para agregar el producto vendido con su precio
def agregar():
    producto=input("ingrese su producto vendido: ")
    precio=input("ingrese el costo del producto: ")
    diccionario = {producto: precio}
    lista_de_productos.append(diccionario)
    main()

#otro para mostrar las ventas de productos con sus respectivos precios.
def mostrar():
    print(lista_de_productos)
    main()

def main():

    accion=int(input("precione |1| para agregar producto vendido\nprecione |2| para mostrar productos vendidos\nprecione |control c| para salir\n: "))
    if accion==1:
        agregar()
            
    elif accion==2:
        mostrar()
    else:
        print("Opción no válida. Intente de nuevo.")

            
if __name__ == "__main__":
    main()


